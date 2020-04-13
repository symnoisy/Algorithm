# AlgorithmService
알고리즘 문제를 풀이하고 REST API로 서비스를 개발합니다.
- JungBeen Yu, MachineLearning/Backend Engineer
- E-Mail: symnoisy@gmail.com / getchabug@gmail.com
- LinkedIn: https://www.linkedin.com/in/jungbeen-yu-614097146/

## How to Start?

#### Service start
<pre><code>
# Execute Docker
> docker pull symnoisy/python:1.0.0
....
> docker run -p 7777:7777 symnoisy/python:1.0.0
 * Serving Flask app "algorithmservicestart.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:7777/ (Press CTRL+C to quit)

or

# Execute Python3.6
> python3.6 algorithmservistart.py

Algorithm Rest API Service start.
Rest Service start. url=http://0.0.0.0:7777/swagger
 * Serving Flask app "algorithmservicestart" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:7777/ (Press CTRL+C to quit)
 
or 
 
# Execute BashScript
> sh ./start_service.sh
> cat algorithmservice.log

Algorithm Rest API Service start.
Rest Service start. url=http://0.0.0.0:7777/swagger
 * Serving Flask app "algorithmservicestart" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:7777/ (Press CTRL+C to quit) 
</code></pre>

#### Enter the service
go to http://0.0.0.0:7777/swagger

#### Enjoy REST APIs

[example1]

<img width="1239" alt="스크린샷 2020-02-27 오전 12 21 23" src="https://user-images.githubusercontent.com/9783553/75359103-3eae5400-58f7-11ea-8fbe-b0f0a0cfa840.png">

[example2]

<img width="1223" alt="스크린샷 2020-02-27 오전 12 23 22" src="https://user-images.githubusercontent.com/9783553/75359198-67cee480-58f7-11ea-9ad6-149c0ae17b79.png">

