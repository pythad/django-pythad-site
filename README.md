This repo servers for some of [Google Code-in](https://developers.google.com/open-source/gci/) 2015 tasks for [FOSSASIA](http://fossasia.org/).

 - Python/Django: Create an About me web app using Django
 - Django: Send an email using django

[Demo](http://pythad-blog.herokuapp.com)

The site is a very basic implementation of personal site built on Django with use of [Bootstap clean blog theme](http://startbootstrap.com/template-overviews/clean-blog/)

To run it locally install all necessary requirements inside your virtualenv with

    pip install -r requirements.txt

then you need to set `HOST_USER` and `HOST_PASSWORD` virtualenv variables so that mail server will work properly. You can do this with

    export HOST_USER='example@example.com'
    export HOST_PASSWORD='password_from_example@example.com'

and after this don't forget to  set `DEBUG` level to `True` in `settings.py`

Screenshots:

###Landing page
![landing page](http://s3.postimg.org/ud4kjp8lf/Selection_019.png)
###Contact form
![contact form](http://s3.postimg.org/vpm9ll60z/Selection_020.png)
###Admin interface with Ckeditor
![admin](http://s3.postimg.org/x5xs3q8xv/Selection_021.png)


