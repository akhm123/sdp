from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8000/adminhome/login/") 
time.sleep(10)
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys("ashishkotecha")
password.send_keys("ashish")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

<div class="navbar navbar-default" role="navigation">
<!-- <div class="container-fluid"> -->
  <div class="navbar-header" >
    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>
    <a class="navbar-brand" href="#">RealLearning</a>
  </div>
  <div class="navbar-collapse collapse">
    <ul class="nav navbar-nav">
<!--       <li class="{% block active_articles %}{% endblock %} active"><a href="">Articles</a></li>
 -->      <li><a href="{%url 'managecourse'%}">Dashboard</a></li>
    </ul>
     <ul class="nav navbar-nav">
     <li><a href="{%url 'logout'%}">logout</a></li>
    </ul>
   <!--  <ul class="nav navbar-nav ">
      <li><a href="{%url 'managecourse'%}">Course</a></li>
    </ul> -->
  </div><!--/.nav-collapse -->
<!-- </div>/.container-fluid  -->
</div>