Movie Recommendation System

A content-based Movie Recommendation System developed using Machine Learning and Natural Language Processing techniques.  
This project recommends movies similar to a selected movie by analyzing movie metadata such as genres, keywords, cast, and crew.

Overview

The recommendation engine uses:

- Text vectorization with `CountVectorizer`
- Similarity calculation using `Cosine Similarity`
- Content-based filtering approach

The application is deployed using Flask and hosted on Render.



Key Features

Personalized movie recommendations  
Content-based filtering system  
NLP-powered similarity engine  
REST API using Flask  
Cloud deployment with Render  
Clean and scalable project structure  



echnologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning utilities |
| CountVectorizer | Text vectorization |
| Cosine Similarity | Recommendation logic |
| Flask | Backend API |
| Git & GitHub | Version control |
| Render | Deployment platform |

---

Project Structure

```bash
movie_recommendation_system/
│
├── app.py
├── movies.pkl
├── requirements.txt
├── Procfile
├── README.md
└── .gitignore