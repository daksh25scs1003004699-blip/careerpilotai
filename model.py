import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MultiLabelBinarizer

ROLES = [
 {"name":"Data Analyst","skills":["Python","SQL","Excel","Statistics","Power BI"],"interests":["Data","Business"],"companies":["Microsoft","Accenture","TCS"],"interview":["Practice SQL joins and aggregations","Clean and visualize a real dataset","Explain business insights and tradeoffs"],"projects":["Sales dashboard","Customer churn analysis"]},
 {"name":"Data Scientist","skills":["Python","SQL","Statistics","Machine Learning","Pandas"],"interests":["Data","AI"],"companies":["Microsoft","Google","Accenture"],"interview":["Explain overfitting and train/test splits","Practice Python and statistics","Discuss evaluation metrics"],"projects":["Customer segmentation","Demand forecasting"]},
 {"name":"Machine Learning Engineer","skills":["Python","Machine Learning","Pandas","Git","Cloud"],"interests":["AI","Software"],"companies":["Google","Microsoft","Amazon"],"interview":["Explain model deployment","Practice Python and ML fundamentals","Understand monitoring and data leakage"],"projects":["Recommendation engine","ML prediction API"]},
 {"name":"Web Developer","skills":["HTML","CSS","JavaScript","React","Git"],"interests":["Web","Design"],"companies":["Amazon","Microsoft","Infosys"],"interview":["Practice JavaScript fundamentals","Explain responsive layouts","Demonstrate deployed websites"],"projects":["Portfolio website","Task manager app"]},
 {"name":"Software Engineer","skills":["Python","Java","C++","DSA","Git"],"interests":["Software","Problem Solving"],"companies":["Google","Microsoft","Amazon","TCS"],"interview":["Practice arrays, trees and graphs","Explain time complexity","Prepare project architecture walkthroughs"],"projects":["File sharing service","Library management system"]},
 {"name":"Cybersecurity Analyst","skills":["Networking","Linux","Python","Cybersecurity","SQL"],"interests":["Security","Problem Solving"],"companies":["IBM","Accenture","TCS"],"interview":["Study TCP/IP and DNS","Explain common web vulnerabilities","Practice ethical security labs"],"projects":["Log anomaly dashboard","Password strength checker"]},
 {"name":"Cloud Engineer","skills":["Linux","Networking","Cloud","Python","Git"],"interests":["Cloud","Software"],"companies":["Amazon","Microsoft","IBM"],"interview":["Explain networking and IAM","Practice deployment workflows","Understand containers and monitoring"],"projects":["Cloud-hosted API","Automated deployment pipeline"]},
 {"name":"UI/UX Designer","skills":["Figma","HTML","CSS","User Research","Prototyping"],"interests":["Design","Web"],"companies":["Google","Microsoft","Accenture"],"interview":["Explain design decisions","Show research and usability testing","Walk through portfolio case studies"],"projects":["App redesign case study","Interactive prototype"]},
 {"name":"Business Analyst","skills":["Excel","SQL","Power BI","Communication","Statistics"],"interests":["Business","Data"],"companies":["Accenture","TCS","Infosys"],"interview":["Practice requirement gathering","Explain KPIs and dashboards","Prepare stakeholder scenarios"],"projects":["Business KPI dashboard","Process improvement study"]},
 {"name":"Mobile App Developer","skills":["Java","Kotlin","Git","SQL","UI Design"],"interests":["Mobile","Software"],"companies":["Google","Amazon","Infosys"],"interview":["Explain app lifecycle","Discuss APIs and local storage","Show a working mobile app"],"projects":["Expense tracker app","Campus event app"]},
 {"name":"DevOps Engineer","skills":["Linux","Git","Docker","Cloud","Python"],"interests":["Cloud","Software"],"companies":["Amazon","Microsoft","IBM"],"interview":["Explain CI/CD","Practice Docker and Linux","Discuss monitoring and rollback"],"projects":["CI/CD demo","Containerized application"]},
 {"name":"QA Automation Engineer","skills":["Python","Java","Testing","Git","SQL"],"interests":["Software","Problem Solving"],"companies":["TCS","Infosys","Accenture"],"interview":["Explain test cases and bug reports","Practice automated tests","Discuss regression testing"],"projects":["Automated web test suite","API test dashboard"]}
]
COMPANIES={
 "Google":"https://www.google.com/about/careers/applications/jobs/results/",
 "Microsoft":"https://careers.microsoft.com/v2/global/en/locations/india.html",
 "Amazon":"https://www.amazon.jobs/",
 "IBM":"https://www.ibm.com/careers/search",
 "Accenture":"https://www.accenture.com/in-en/careers/jobsearch",
 "TCS":"https://www.tcs.com/careers",
 "Infosys":"https://www.infosys.com/careers/"
}
ALL_SKILLS=sorted({s for role in ROLES for s in role['skills']})
ALL_INTERESTS=sorted({i for role in ROLES for i in role['interests']})
mlb=MultiLabelBinarizer(classes=ALL_SKILLS)
mlb.fit([ALL_SKILLS])
X=mlb.transform([r['skills'] for r in ROLES]).astype(float)
# Interest is a small additional preference signal, not a hiring qualification.
interest_vectors=np.array([[float(i in r['interests']) for i in ALL_INTERESTS] for r in ROLES])
features=np.hstack([X, 0.4*interest_vectors])
knn=NearestNeighbors(n_neighbors=len(ROLES),metric='cosine')
knn.fit(features)

def recommend(skills, interests, limit=8):
    if not skills:
        return []
    query=np.hstack([mlb.transform([skills])[0].astype(float),
                     0.4*np.array([float(i in interests) for i in ALL_INTERESTS])])
    distances,indices=knn.kneighbors([query],n_neighbors=len(ROLES))
    results=[]
    for distance,idx in zip(distances[0],indices[0]):
        role=ROLES[int(idx)].copy()
        role['score']=round(max(0,1-float(distance))*100)
        role['matched']=sorted(set(skills)&set(role['skills']))
        role['missing']=sorted(set(role['skills'])-set(skills))
        results.append(role)
    return results[:limit]
