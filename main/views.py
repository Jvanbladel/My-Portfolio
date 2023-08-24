from django.shortcuts import render

HTML_EXT = ".html"

context = {}

project_list = [
    {
        "name": "Stock Market Risk Analyzer",
        "short_description": "This data science research created a predictive model using regression and statistical analysis to quantify stock market risk, aiding investors in assessing security risks.",
        "img": "images/risk_analyzer_project.png",
        "href": "/risk-analyzer",
    },
    {
        "name": "Real-Time Weather",
        "short_description": "The Real-Time Weather Dashboard is a web application that provides users with up to date weather data for any location or city showcasing my understanding and implementation of API's.",
        "img": "images/weather_project.png",
        "href": "/weather",
    },
    {
        "name": "Auction House Website",
        "short_description": "Full Stack development demonstrating my skills in Django using the Model View Template (MVT) architecture.",
        "img": "images/auction_house_project.png",
        "href": "/auction-house",
    },
    {
        "name": "Tank Shooting Simulator",
        "short_description": "Coordinate and develop a program that implements a graphical interface.",
        "img": "images/tank_project.png",
        "href": "/epic-tanks",
    },
    {
        "name": "Starving Steve",
        "short_description": "Understand human interface design.",
        "img": "images/starving_steve_project.jpg",
        "href": "/starving-steve",
    },
    {
        "name": "Immunization Compliance",
        "short_description": "Developed healthcare software",
        "img": "images/ica_project.png",
        "href": "/immunization-compliance",
    },
]


def index(request):
    context["my_view_name"] = "index"
    return render(request, gethtmlpath(context["my_view_name"]), context)


def work(request):
    context["my_view_name"] = "work"
    context["project_list"] = project_list
    return render(request, gethtmlpath(context["my_view_name"]), context)


def resume(request):
    context["my_view_name"] = "resume"
    return render(request, gethtmlpath(context["my_view_name"]), context)


def contact(request):
    context["my_view_name"] = "contact"
    return render(request, gethtmlpath(context["my_view_name"]), context)


def gethtmlpath(current_page):
    return current_page + "/" + current_page + HTML_EXT


# {
#        "name": "Canny Edge Detector",
#        "short_description": "To utilize parallelization methods to speed up execution of image outlining algorithm.",
#        "img": "images/hpc_output.png",
#        "href": "/canny-edge-detector",
#    },
