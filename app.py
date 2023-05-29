from flask import Flask, render_template , jsonify

app = Flask(__name__)

JOBS = [
{
  'id':1,
  'title': 'Data Analyst',
  'location': ' Orchard ,Singapore',
  'salary': '$10,000/month'
},
  {
  'id':2,
  'title': 'Data Scientist',
  'location': ' City Hall ,Singapore',
  'salary': '$12,000/month'  
  },
{
  'id':3,
  'title': 'Financial Analyst',
  'location': ' Orchard ,Singapore',
  'salary': '$10,000/month'
},
  {
  'id':4,
  'title': 'Portfolio Mananger',
  'location': ' Orchard ,Singapore',
  'salary': '$14,000/month'  
  }
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS,company_name='Isaac') 

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
