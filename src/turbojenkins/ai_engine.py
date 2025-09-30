"""AI engine that calls Google Generative AI (Gemini) for suggestions."""
import os

SYSTEM_PROMPT = """
You are an expert DevOps engineer specializing in Jenkins pipeline optimization.
Analyze the provided Jenkinsfile and suggest specific improvements focusing on:
1) Parallelization
2) Caching strategies
3) Resource selection
4) Declarative vs scripted conversion
Return concise recommendations with estimated time savings.
"""

try:
    import google.generativeai as genai  # type: ignore
except Exception:  # pragma: no cover - allow tests without package
    genai = None


def ask_optimization(pipeline_name: str, jenkinsfile: str, avg_time_min: float) -> str:
    key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not key:
        return "GEMINI_API_KEY or GOOGLE_API_KEY not set; cannot call Gemini."

    if genai is None:
        return "google-generativeai package not installed; please pip install google-generativeai."

    genai.configure(api_key=key)
    model = os.getenv("GEMINI_MODEL", "gemini-1.5")

    user_content = (
        f"Pipeline: {pipeline_name}\n"
        f"AvgBuildMinutes: {avg_time_min:.2f}\n\n"
        f"Jenkinsfile:\n{jenkinsfile}\n\n"
        "Provide up to 3 concise optimization recommendations with estimated time savings."
    )

    try:
        response = genai.generate_text(
            model=model,
            temperature=0.1,
            max_output_tokens=800,
            prompt=SYSTEM_PROMPT + "\n\n" + user_content,
        )

        if hasattr(response, "text") and response.text:
            return response.text.strip()
        if hasattr(response, "candidates") and response.candidates:
            first = response.candidates[0]
            if hasattr(first, "content"):
                return first.content.strip()
            if hasattr(first, "output"):
                return first.output.strip()
        return str(response).strip()
    except Exception as e:
        return f"Gemini call failed: {e}"
