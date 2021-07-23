# Reddit Account Generator
 **WHAT IS IT?**
 
 This is a semi-automatic Reddit account generator. I'm saying "semi-automatic" because it still requires a Google Captcha to be completed at the end of the creation process.
 
 **HOW DOES IT WORK?**
 
 This script was made for quickly creating Reddit throwaways. _See my other project -- the Reddit Account Deleter, which is made to completly erase Reddit accounts (including comments and all)._
 It generates an username derived from a Wikipedia:Random article, and then appending some random digits to it as to have it be unique. Then, it completes the Reddit sign-up process, leaving you only to complete the Captcha at the end.
 
 **REQUIRMENTS**
 
 Only Selenium and webdriver-manager (pip install selenium && pip install webdriver-manager).
 A file named "namesforreddit.txt" should be in the same folder as the .py executable.
 
 **UPDATES**
 
_23.7.2021_ - 
 Reviewed the almost year-old code and made some small changes. Now, it should be more stable, as it doesn't use XPaths anymore.
 Also, because I've added Webdriver-Manager there should be less (or none?) inconstencies between the driver versions, as it automatically updates the version of the webdriver with every launch.
 
 Hopefully this is useful; feedback kindly appreciated :)
