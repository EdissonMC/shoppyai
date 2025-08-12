# ConversaShop AI - Intelligent Multi-Vendor Marketplace

> **AI-Powered E-commerce Platform** where customers **chat with intelligent agents** to discover and purchase products across multiple vendors seamlessly.

## 🎯 Project Overview

**ConversaShop AI** is a modern e-commerce marketplace that revolutionizes online shopping through **conversational AI**. Instead of traditional search and filtering, customers engage in natural conversations with AI agents that understand their needs, recommend products, and guide them through the entire purchase journey.

### 🚀 Key Features

- **🤖 Intelligent Chat Agents**: LangChain-powered AI agents that understand customer intent
- **🏪 Multi-Vendor Platform**: Native multi-vendor support with automated commission splits
- **🔍 Hybrid Search**: Combines vector search (RAG) with traditional SQL and full-text search
- **⚡ Real-time Chat**: WebSocket-powered instant messaging with typing indicators
- **🎨 Modern UI**: Next.js frontend with responsive, mobile-first design
- **☁️ Cloud-Ready**: Containerized architecture optimized for AWS deployment

## 🏗️ Architecture

### Microservices Architecture
```
┌─────────────────┬─────────────────┬─────────────────┐
│   FRONTEND      │   DJANGO API    │   FASTAPI AI    │
│   (Next.js)     │   (E-commerce)  │   (Agents)      │
├─────────────────┼─────────────────┼─────────────────┤
│ • React/TypeScript │ • Multi-vendor  │ • LangChain     │
│ • Real-time Chat   │ • Product Mgmt  │ • Vector Search │
│ • Responsive UI    │ • Order Process │ • OpenAI/Claude │
│ • State Mgmt       │ • Admin Panel   │ • WebSockets    │
└─────────────────┴─────────────────┴─────────────────┘
```

### Tech Stack
- **Frontend**: Next.js 14, TypeScript, Tailwind CSS, React Query
- **Backend API**: Django 4.2, Django REST Framework, PostgreSQL
- **AI Engine**: FastAPI, LangChain 0.3, OpenAI/Claude, ChromaDB
- **Infrastructure**: Docker, AWS ECS, RDS, ElastiCache, CloudFront
- **Development**: Python 3.11+, Node.js 18+, Git, VS Code

## 🎯 Business Problem Solved

### Current E-commerce Pain Points:
- **85% of searches fail** to show relevant products
- **44% of users spend 3+ minutes** finding what they need
- **98% of visitors leave** without purchasing anything
- **Insufficient product information** is the #1 complaint

### Our Solution:
✅ **Conversational Discovery**: Natural language product search  
✅ **Intelligent Recommendations**: AI explains why products match needs  
✅ **Contextual Understanding**: Learns from user behavior and preferences  
✅ **Seamless Multi-vendor**: Single checkout for multiple sellers  

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- OpenAI API Key

### 1. Clone & Setup
```bash
git clone https://github.com/your-username/conversashop-ai.git
cd conversashop-ai
```

### 2. AI Engine Setup
```bash
cd ai-engine
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # macOS/Linux
pip install -r requirements.txt
```

### 3. Environment Configuration
```bash
# Copy and configure environment variables
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 4. Run Development Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

### 5. Test the API
```bash
curl -X POST "http://localhost:8001/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "I need a comfortable office chair under $300"}'
```

## 📊 Project Status

### ✅ MVP Phase 1 - Completed
- [x] Project structure and architecture design
- [x] FastAPI + LangChain integration
- [x] Basic chat agent with OpenAI
- [x] Environment setup and dependencies
- [x] Docker containerization ready

### 🔄 Phase 2 - In Progress
- [ ] Django backend with multi-vendor models
- [ ] Product catalog and vendor management
- [ ] Advanced AI agents (RAG, Actions, Analytics)
- [ ] Next.js frontend with chat interface

### 📋 Phase 3 - Planned
- [ ] Real-time WebSocket chat
- [ ] Vector database integration (ChromaDB)
- [ ] Payment processing integration
- [ ] AWS deployment pipeline

## 🛠️ Development

### API Documentation
- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc

### Testing
```bash
# Run tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html
```

### Code Quality
```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

## 🌟 Why This Project?

### For Portfolio Demonstration:
- **Modern Architecture**: Microservices, AI integration, cloud-native
- **Full-Stack Skills**: Frontend, Backend, AI, DevOps
- **Business Value**: Solves real e-commerce problems
- **Scalable Design**: Production-ready architecture
- **Current Technologies**: LangChain, FastAPI, Next.js, AWS

### Technical Learning Outcomes:
- Advanced Django ORM with complex relationships
- LangChain and AI agent orchestration
- Real-time WebSocket communication
- Vector databases and semantic search
- Modern frontend development with TypeScript
- Containerization and cloud deployment
- API design and microservices patterns

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 👤 Author

**Edison** - Full-Stack Developer specializing in AI-powered applications

- Portfolio: [your-portfolio-url]
- LinkedIn: [your-linkedin]
- GitHub: [your-github]

---

*Built with ❤️ using Django, FastAPI, LangChain, and Next.js*
