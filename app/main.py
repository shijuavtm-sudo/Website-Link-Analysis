from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from app.schemas import LinkRequest
from app.services.website_extractor import extract_website_content
from app.services.llm_services import analyze_website

app = FastAPI(title="AI Website Link Analysis")


@app.get("/")
async def home():
    return FileResponse("app/templates/index.html")


@app.post("/link-analysis")
async def link_analysis(request: LinkRequest):
    try:
        url = str(request.url)

        # Step 1: Extract website content
        website_data = await extract_website_content(url)

        # Step 2: Analyze using Groq
        analysis = await analyze_website(website_data)

        # Step 3: Return structured response
        return {
            "success": True,
            "website": url,
            "brand": {
                "name": website_data["title"],
                "category": "AI identified",
                "summary": website_data["description"],
            },
            "analysis": analysis,
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Website analysis failed: {str(e)}",
        )