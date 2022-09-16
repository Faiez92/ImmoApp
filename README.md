# ImmoApp
ImmoApp application for test


To launch ImmoApp application you need to follow these steps:

    1- git clone git@github.com:Faiez92/ImmoApp.git
    2- execute the command 'docker-compose up' # the build will be executed and run #
    3- type in browser 0.0.0.0:8000 where you can find the home page containing buttons to gide you in your visit

to launch test you need a new terminal:
    
    1- execute the command 'docker exec -it immoapp_web_1 bash'
    2- execute the command 'export DJANGO_SETTINGS_MODULE=ImmoApp.settings'
    3- execute the command 'pytest'
        


Thank you for your time
    
    
                                                                            Mohamed Faiez ABID