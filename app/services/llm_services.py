import json
from groq import AsyncGroq

from app.config import GROQ_API_KEY, GROQ_MODEL

client = AsyncGroq(api_key=GROQ_API_KEY)


async def analyze_website(website_data):
    prompt = f"""
You are an expert website, SEO and business analyst.

Analyze the following website information.

WEBSITE TITLE:
{website_data['title']}

WEBSITE DESCRIPTION:
{website_data['description']}

WEBSITE CONTENT:
{website_data['content']}

Generate a meaningful analysis using these five sections.

1. competitor_analysis:
   - brand_overview
   - competitors (minimum 3 where reliable information is available)
   - strengths
   - opportunities

2. target_search_queries:
   Generate 5 relevant queries. Include query, platforms, intent,
   business_relevance and target_audience.
   Support Google, Facebook, Instagram, LinkedIn and X.

3. seo_improvements:
   - primary_keyword
   - secondary_keywords
   - long_tail_keywords
   - recommended_title
   - meta_description
   - supporting_content

4. top_services:
   Generate up to 5 relevant services. Include service_name, description,
   target_industry, target_customer and main_benefit.

5. target_audience:
   - primary_audience
   - secondary_audience
   - industries
   - business_types
   - customer_needs
   - geographical_focus

IMPORTANT:
- Base the analysis on the actual website content.
- Do not invent facts or search volumes.
- If information is missing, say it is unavailable.
- Clearly label inferred recommendations.
- Competitors must be identified as AI suggestions unless independently verified.
- Return only valid JSON.
"""

    response = await client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a professional website analysis AI.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.2,
        max_completion_tokens=5000,
        response_format={"type": "json_object"},
    )

    result = response.choices[0].message.content

    return json.loads(result)