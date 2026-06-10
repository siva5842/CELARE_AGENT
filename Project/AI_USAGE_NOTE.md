# 🤖 AI Usage Note & Project Logs

**Team:** Kinetic Prism
**Date:** June 9, 2026
**AI Model Used:** Trae AI Assistant 

## 1. AI Pair-Programming Strategy
We utilized a **Driver/Navigator** framework adapted for AI. One team member engineered the context prompts (Driver), while the other members QA'd the test outputs and validated the architecture (Navigators). We utilized Git `Co-authored-by` trailers via terminal automation to accurately reflect team consensus.

## 2. Structural Successes
* **Dynamic Structural Masking:** Instructed the AI to use random symbol generation (`*`, `#`, `X`) combined with Regex capture groups (`\g<1>`) to create professional masks (e.g., `AXXXXXXXK`) instead of generic redaction blocks.
* **Agent Loop Integration:** Successfully built a deterministic while-loop in Python that reprompts the local Ollama LLM if entity extraction confidence falls below 85%.

## 3. Edge-Case Errors & AI Hallucinations Corrected
* **UI CSS Rendering Crashes:** The AI attempted to aggressively style Streamlit using raw CSS, corrupting the React frontend. **Fix:** Promoted the AI to revert to native Streamlit container layouts.
* **Pandas Float Artifacts:** The AI's regex failed on phone numbers because Pandas converted them to floats (adding `.0`). **Fix:** Instructed the AI to implement `df.astype(str).replace(r'\.0$', '', regex=True)` before regex execution.
* **Aadhaar Spacing Issues:** The initial `\b` (word boundary) regex failed when Aadhaar numbers contained spaces or hyphens. **Fix:** Engineered a prompt utilizing negative lookbehinds `(?<!\d)` and non-capturing groups `(?:...)` to force the engine to ignore structural separators.

## 4. Best Prompts Used
> *"Find the Aadhaar masking logic and replace it entirely with a pattern that uses a non-capturing group `(?:...)` for the middle digits and spaces, ensuring that no matter how the Aadhaar is formatted, the first two and last two digits are perfectly captured in `\g<1>` and `\g<2>`."*