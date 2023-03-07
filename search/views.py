# Django imports.
from django.http import JsonResponse

# Third party imports.
import json

# This module imports.
from .APIsearch import APISearchQLD, WebScrapeSearchQLD, Add, RetreiveAllQLD, ResultEncoder


# Other module imports.
from data_extraction.models import *
from data_extraction.functions import ConvertToTrueFalse
from data_extraction.responseCodes import Result, GenerateResult, PrintResultLog, searchList as resultList

# Create your views here.
def SearchGov(request):
    # Load request variables.
    data = json.loads(request.body.decode("utf-8"))

    searchStr=data['searchStr']
    method = data['method']
    attachmentsOnlyStr = data['attachmentsOnly']
    WCRonlyStr = data['WCRonly']
    includeExistingStr = data['includeExisting']

    # Convert Y/N to True/False.
    attachmentsOnly = ConvertToTrueFalse(attachmentsOnlyStr)
    WCRonly = ConvertToTrueFalse(WCRonlyStr)
    includeExisting = ConvertToTrueFalse(includeExistingStr)

    # Select the appropriate search method.
    if(method == "Web"):
        # Note web scrapping is not currently being developed as the API has now been rolled out.
        mySearch = WebScrapeSearchQLD(searchStr, attachmentsOnly, WCRonly, includeExisting)
    else:
        mySearch = APISearchQLD(searchStr,attachmentsOnly, WCRonly, includeExisting)

    # Run the search.
    mySearch.search()

    # Put the results into a reponse.
    response = {'searchName':repr(mySearch),'results':ResultEncoder().encode(mySearch)}

    # Convert to Json and return the response.
    return JsonResponse(response)

def AddDatabase(request, state, pid):
    package = Package.objects.filter(gov_id=pid).first()
    if package is None:
        check = False
        try:
            package = Package.objects.create(gov_id=pid)
            check=True
        except Exception as e:
            result = GenerateResult(resultList,36)
            PrintResultLog(result)
        
        if check:
            response = Add(package,state)
            return JsonResponse(response)
    else:
        response = Add(package,state)
        return JsonResponse(response)

    response = None
    return JsonResponse(response)
    

def ManualAdd(request,id):

    response = Add(id,"QLD")

    # Convert to Json and return the response.
    return JsonResponse(response)

def AddMany(request):
    data = json.loads(request.body.decode("utf-8"))

    wellList = data['wellList']

    responseList = []

    for well in wellList:
        response = Add(well['id'],well['state'] )
        responseList.append(response)

    response = {'results':ResultEncoder().encode(responseList)}

    return JsonResponse(response)
    
def UpdateAllQLD(request):
    responseList = RetreiveAllQLD()
    print(responseList)
    
    return JsonResponse(responseList, safe=False)

    #response = {'results':ResultEncoder().encode(responseList)}
    #return JsonResponse(response, safe=False)





