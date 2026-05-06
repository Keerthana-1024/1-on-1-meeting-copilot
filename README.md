# 🌱 IntelliGrow

**IntelliGrow** is an AI-powered, unified performance management and upskilling platform. Designed to seamlessly connect appraisals, 1-on-1 meetings, and personalized learning, IntelliGrow empowers managers and reportees to foster continuous professional development through intelligent data synthesis.

---

## ✨ Core Features

### 📊 1. Smart Dashboards
IntelliGrow offers distinct, role-based contextual views that update in real-time:
- **Reportee View (`dashboard.html`)**: Tracks personal VED (Value, Execution, Domain) competencies, overall momentum, and upcoming deliverables.
- **Manager View (`manager_dashboard.html`)**: Provides a team-wide overview, appraisal drafting interfaces, and meeting scheduling tools.
- **Dynamic Workflows**: Status-based routing for meetings (e.g., `form_not_provided`, `active`, `completed`) to guide users seamlessly through the performance review lifecycle.

### 🎙️ 2. AI Meeting Copilot (STT)
Never lose track of what was discussed in a 1-on-1 again.
- **Real-time Transcription**: Deepgram integration captures live meeting audio, automatically identifying speakers.
- **Automated Summaries & Action Items**: Post-meeting, the AI backend synthesizes the raw transcript into concise summaries and extracts actionable items.
- **Unified Storage**: All transcripts, summaries, and action items are natively stored in Supabase for reliable, secure access without external dependency risks.

### 🎓 3. Personalized Learning Module
Action items directly fuel professional growth.
- **Contextual Course Recommendations**: Based on your appraisal scores and meeting action items, IntelliGrow recommends tailored courses.
- **Provider Integrations**: Extensive library mockups including Coursera, edX, Udemy, YouTube, and TNQ Academy.
- **Progress Tracking**: Track course completions and view customized interactive quizzes to validate learning retention directly within the platform.

### 💬 4. "Chat with Data" (RAG Interface)
A ChatGPT-style conversational assistant embedded directly into the dashboards.
- **Role-Aware Context**: The chatbot adapts its context whether you are querying as a manager (e.g., *"How is my team performing?"*) or a reportee (e.g., *"How should I prepare for my next 1-on-1?"*).
- **Intelligent Synthesis**: Seamlessly pulls from historical appraisals, meeting transcripts, and learning progress to provide highly actionable, personalized advice.
- **Future-Ready Architecture**: UI built to support an upcoming integration with `pgvector` and `mem0` for advanced Retrieval-Augmented Generation (RAG).

---

## 🛠️ Tech Stack & Architecture

- **Frontend**: Vanilla HTML5, CSS3, and Javascript. Built with a focus on a "glassmorphic," premium, and highly responsive user experience. No bulky frameworks.
- **Backend Framework**: Python **FastAPI**.
- **Database**: **Supabase** (PostgreSQL). Stores users, meeting transcripts, action items, and learning metadata.
- **AI/ML**: 
  - **Deepgram API** for low-latency Speech-to-Text (STT).
  - **Google Gemini** for text synthesis, summarization, and RAG capabilities.

---

## 🚀 Setup & Local Development

### Prerequisites
- Python 3.9+
- A Supabase account and project
- Deepgram API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/intelligrow.git
   cd intelligrow
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```ini
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_anon_key
   DEEPGRAM_API_KEY=your_deepgram_key
   GEMINI_API_KEY=your_gemini_key
   ```

4. **Run the Backend Server**
   To serve the environment variables dynamically and handle backend routes, use Uvicorn:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   *Note for WSL users: Ensure your port forwarding is correctly configured if accessing from a Windows browser.*

5. **Access the Application**
   Navigate to `http://localhost:8000/role_select.html` to begin using the application.

---

## 🗺️ Roadmap & Next Steps
- [ ] **Full RAG Backend Integration**: Hook up the current "Chat with Data" UI to a real `pgvector` + `mem0` backend pipeline to dynamically embed and retrieve transcripts.
- [ ] **Live Quiz Database Integration**: Migrate the hardcoded learning quizzes to dynamic, LLM-generated questions stored in Supabase.
- [ ] **Production Deployment**: Finalize CI/CD pipelines for deployment to Render.
