# IntelliGrow

**Performance Management & Upskilling Engine**
*RAG Architecture | Real-Time Diarization | Multi-Agent LLM Processing | Hybrid RecSys*

IntelliGrow is an enterprise-grade performance management platform that unifies 1-on-1 meeting intelligence, contextual upskilling, and conversational data querying into a single, automated ecosystem.

---

## System Architecture & Capabilities

### 1. Real-Time Speech Processing Pipeline
The meeting copilot relies on low-latency audio processing for live transcription.
- **WebSocket Streaming**: Continuous audio streaming over WebSockets ensures minimal latency during active 1-on-1 meetings.
- **Deepgram & Diarization**: High-accuracy Speech-to-Text (STT) utilizing native speaker diarization to separate and identify manager versus reportee dialogue.
- **Session Tracking**: Links live audio streams with specific meeting IDs, ensuring secure and precise transcript routing directly into the database.

### 2. Multi-Agent Data Synthesis
Post-meeting data is processed using a sophisticated, chained LLM architecture.
- **Processing Flow**: Raw meeting transcripts are passed through chained prompts to generate structured Meeting Summaries and automatically extract Action Items.
- **Extensibility**: Currently utilizing Gemini for prompt logic and synthesis. The system is designed to allow drop-in replacements with fine-tuned models optimized for domain-specific corporate terminology in the future.
- **Unified Data Stores**: Transcripts, Summaries, Action Items, and Manager Review Remarks (captured via post-meeting forms) are persistently stored in Supabase PostgreSQL.

### 3. "Chat with Data" (RAG Backend)
A highly contextual Retrieval-Augmented Generation (RAG) system built to synthesize heterogeneous performance data across the employee lifecycle.
- **Data Ingestion Sources**: Embeds and indexes Meeting Transcripts, Summaries, Action Items, Manager Remarks, and Course Completion metrics.
- **Vector & Memory Infrastructure**: Powered by **pgvector** and **mem0**. `mem0` abstracts entity extraction and long-term memory management, while `pgvector` handles the underlying high-dimensional semantic similarity search within Supabase.
- **Dual Query Modes**: 
  - *Reportee Context*: Optimized for task execution, 1-on-1 preparation, and specific feedback analysis.
  - *Manager Context*: Optimized for team performance tracking, identifying cross-team upskilling gaps, and drafting review agendas.

### 4. Recommendation System (RecSys) & Learning
The learning module leverages automated skill-matching to drive professional development.
- **Action Item to Course Mapping**: Utilizes a hybrid mapping logic (combining NLP entity extraction with vector DB semantic matching) to align extracted meeting action items directly with external course catalogs (Coursera, edX, Udemy).
- **Dynamic Assessment**: Features an LLM-driven logic engine to dynamically generate contextual quizzes based on recently completed courses, validating knowledge retention.

---

## Tech Stack

- **Backend Framework**: Python FastAPI
- **Database**: Supabase (PostgreSQL, pgvector)
- **AI/ML Layer**: Deepgram (Websocket STT), Gemini (LLM & Embeddings), mem0 (Memory Management)
- **Frontend**: Vanilla HTML5, CSS3, Javascript (Dashboard UI)

---

## Local Setup & Development

### Prerequisites
- Python 3.9+
- Supabase account and project
- Deepgram API Key
- Gemini API Key

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
   Navigate to `http://localhost:8000/role_select.html` to access the dashboards.
