# Ex.04 Design a Website for Server Side Processing
## Date:10.12.25

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```

math.html

<html>
<head>
    <title>MILEAGE CALCULATOR</title>
    <style>
        .head{
            gap:30;
            position: fixed;
            top:22%;
            right: 40%;
            border: solid  4px yellow;
            border-radius: 20px;
            background: lightskyblue;
        }
        input {
            margin-top: 5px;
            padding: 10px;
            border-radius: 20px;
        }
        body {
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            background-color: cyan;
        }
        .form{
            border-radius: 30px;
            width: 400px;
        }
        .submit{
            color: red;
            background-color: lightblue;
        }
    </style>
</head>
<body>
    <center>
    <div class="head">
        <h1><u>MILEAGE CALCULATOR</u></h1>
        <h2>POOJA D</h2>
        <h2>(25016436)</h2>

        <form method="POST">

                {% csrf_token %}
                <label>Distance Travelled:</label>
                <input type="number" value="{{D}}" name="distance_travelled">in (km)
                <br>

                <label>Fuel Consumed:</label>
                <input type="number" name="fuel_consumed" value="{{f}}">in (l)
                <br><br>

                <input type="submit" value="Calculate">
                <br>

                <label>Mileage:</label>
                <input type="number" name="m" value="{{m}}"> in (km/l)

            </form>

    </div>
    </center>
</body>
</html>
```
```
views.py

from django.shortcuts import render
def efficiency(request):
    D=int(request.POST.get('distance_travelled',0))
    f=int(request.POST.get('fuel_consumed',0))
    m=D/f if request.method=='POST' else 0
    print("Distance travelled=",D)    
    print("Fuel consumed=",f)
    print("Mileage=",m)
    return render(request,'mathapp/math.html',{'D':D,'f':f,'m':m})

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns= [path('admin/', admin.site.urls),
path('',views.efficiency,name='efficiency'),]

```


## OUTPUT - SERVER SIDE:
Screenshot 2025-12-09 203305.png

## OUTPUT - WEBPAGE:
Screenshot 2025-12-09 203324.png

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
