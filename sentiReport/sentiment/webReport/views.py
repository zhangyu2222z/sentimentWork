from django.shortcuts import render
from django.http import JsonResponse
from .models import TClnProductInfo, TProductInfo
from django.db.models import Count
# Create your views here.

def index(request):
    return render(request, 'index.html')

def queryStatistic(request):
    _productName = request.GET.get('productName')
    _productWords = request.GET.get('productWords')
    _productTime = request.GET.get('productTime')
    condtions = {}
    p_code_condition = []
    if _productName is not None and _productName != '':
        print(_productName)
        pCode = TProductInfo.objects.filter(productname__contains=_productName).get().productcode
        if pCode is not None:
            condtions['productcode__contains'] = pCode
        p_code_condition.append(pCode)
        total = TClnProductInfo.objects.filter(productcode__in=p_code_condition).aggregate(Count('productcode'))
    else:
        p_code_list = TClnProductInfo.objects.values('productcode').annotate(p_num=Count("productcode")).order_by("-p_num")[:10]
        for elem in p_code_list:
            p_code_condition.append(elem['productcode'])
        total = TClnProductInfo.objects.filter(productcode__in=p_code_condition).aggregate(Count('productcode'))

    if _productWords is not None and _productWords != '':
        condtions['comments__contains'] = _productWords
    if _productTime is not None and _productTime != '':
        condtions['commenttime__contains'] = _productTime
    if len(condtions) > 0:
        print(condtions)
        ret1 = TClnProductInfo.objects.values().filter(productcode__in=p_code_condition).filter(**condtions).filter(sentiments=1).aggregate(Count('sentiments'))
        ret2 = TClnProductInfo.objects.values().filter(productcode__in=p_code_condition).filter(**condtions).filter(sentiments=0).aggregate(Count('sentiments'))
    else:
        ret1 = TClnProductInfo.objects.values().filter(productcode__in=p_code_condition).filter(sentiments=1).aggregate(Count('sentiments'))
        ret2 = TClnProductInfo.objects.values().filter(productcode__in=p_code_condition).filter(sentiments=0).aggregate(Count('sentiments'))
    if int(ret1['sentiments__count']) > int(ret2['sentiments__count']):
        main_val = '偏好'
    else:
        main_val = '偏差'

    total_cnt = (int(ret1['sentiments__count']) + int(ret2['sentiments__count']))
    if total_cnt > 0:
        pos = round(int(ret1['sentiments__count']) / total_cnt, 4)*100
        neg = round(int(ret2['sentiments__count']) / total_cnt, 4)*100
    else:
        pos = 0
        neg = 0
    ret_dict = {"total":total['productcode__count'], "main":main_val, "pos":f'{pos}%', "neg":f'{neg}%'}
    return JsonResponse(ret_dict)

# def queryAreaChart(request, productName, productWords, productTime):
def queryAreaChart(request):
    print("===================================in queryAreaChart")
    _productName = request.GET.get('productName')
    _productWords = request.GET.get('productWords')
    _productTime = request.GET.get('productTime')
    condtions = {}
    labels = []
    p_code_condition = []
    if _productName is not None and _productName != '':
        pCode = TProductInfo.objects.filter(productname__contains=_productName).get().productcode
        if pCode is not None:
            condtions['productcode__contains'] = pCode
        p_code_condition.append(pCode)
        pName = TProductInfo.objects.filter(productname__contains=_productName).get().productname
        labels.append({'productname':pName, 'productcode':pCode})
    else:
        p_code_list = TClnProductInfo.objects.values('productcode').annotate(p_num=Count("productcode")).order_by("-p_num")[:10]
        for elem in p_code_list:
            p_code_condition.append(elem['productcode'])
        p_list = list(TProductInfo.objects.filter(productcode__in=p_code_condition).iterator())
        for p in p_list:
            labels.append({'productname':p.productname, 'productcode':p.productcode})
    if _productWords is not None and _productWords != '':
        condtions['comments__contains'] = _productWords
    if _productTime is not None and _productTime != '':
        condtions['commenttime__contains'] = _productTime
    if len(condtions) > 0:
        ret = TClnProductInfo.objects.filter(productcode__in=p_code_condition).filter(**condtions).values('productcode').annotate(p_code_cnt=Count('productcode')).iterator()
    else:
        ret = TClnProductInfo.objects.filter(productcode__in=p_code_condition).values('productcode').annotate(p_code_cnt=Count('productcode')).iterator()
    ret_list = list(ret)
    vals_list = []
    label_vals = []
    for item in labels:
        for r in ret_list:
            if item['productcode'] == r['productcode']:
                label_vals.append(item['productcode'])
                # label_vals.append(item['productname'])
                vals_list.append(r['p_code_cnt'])
    ret_dict = {"labels":labels, "vals":vals_list}
    print(ret_dict)
    return JsonResponse(ret_dict)

# def queryBarChart(request, productName, productWords, productTime):
def queryBarChart(request):
    print("===================================in queryBarChart")
    _productName = request.GET.get('productName')
    _productWords = request.GET.get('productWords')
    _productTime = request.GET.get('productTime')
    condtions = {}
    labels = []
    p_code_condition = []
    if _productName is not None and _productName != '':
        pCode = TProductInfo.objects.filter(productname__contains=_productName).get().productcode
        if pCode is not None:
            condtions['productcode__contains'] = pCode
        pName = TProductInfo.objects.filter(productname__contains=_productName).get().productname
        labels.append({'productname':pName, 'productcode':pCode})
        p_code_condition.append(pCode)
    else:
        p_code_list = TClnProductInfo.objects.values('productcode').annotate(p_num=Count("productcode")).order_by("-p_num")[:10]
        for elem in p_code_list:
            p_code_condition.append(elem['productcode'])
        p_list = list(TProductInfo.objects.filter(productcode__in=p_code_condition).iterator())
        for p in p_list:
            labels.append({'productname':p.productname, 'productcode':p.productcode})
    if _productWords is not None and _productWords != '':
        condtions['comments__contains'] = _productWords
    if _productTime is not None and _productTime != '':
        condtions['commenttime__contains'] = _productTime
    if len(condtions) > 0:
        pos_ret = TClnProductInfo.objects.filter(productcode__in=p_code_condition).filter(**condtions).filter(sentiments='1').values('productcode').annotate(p_code_cnt=Count('productcode')).iterator()
        neg_ret = TClnProductInfo.objects.filter(productcode__in=p_code_condition).filter(**condtions).filter(sentiments='0').values('productcode').annotate(p_code_cnt=Count('productcode')).iterator()
    else:
        pos_ret = TClnProductInfo.objects.filter(productcode__in=p_code_condition).filter(sentiments='1').values('productcode').annotate(p_code_cnt=Count('productcode')).iterator()
        neg_ret = TClnProductInfo.objects.filter(productcode__in=p_code_condition).filter(sentiments='0').values('productcode').annotate(p_code_cnt=Count('productcode')).iterator()
    ret = {}
    vals1 = [0,0,0,0,0,0,0,0,0,0]
    vals2 = [0,0,0,0,0,0,0,0,0,0]
    label_vals = []
    pos_list = list(pos_ret)
    neg_list = list(neg_ret)
    for item in range(len(labels)-1):
        for r in pos_list:
            if labels[item]['productcode'] == r['productcode']:
                vals1[item] = r['p_code_cnt']
        for m in neg_list:
            if labels[item]['productcode'] == m['productcode']:
                vals2[item] = m['p_code_cnt']
        # label_vals.append(labels[item]['productcode'])
        # productname
    ret['vals1'] = vals1
    ret['vals2'] = vals2
    ret['labels'] = labels
    print(ret)
    return JsonResponse(ret)

# def queryDetails(request, productName, productWords, productTime):
def queryDetails(request):
    _productName = request.GET.get('productName')
    _productWords = request.GET.get('productWords')
    _productTime = request.GET.get('productTime')
    condtions = {}
    p_code_condition = []
    if _productName is not None and _productName != '':
        pCode = TProductInfo.objects.filter(productname__contains=_productName).get().productcode
        if pCode is not None:
            condtions['productcode__contains'] = pCode
        p_code_condition.append(pCode)
    else:
        p_code_list = TClnProductInfo.objects.values('productcode').annotate(p_num=Count("productcode")).order_by("-p_num")[:10]
        for elem in p_code_list:
            p_code_condition.append(elem['productcode'])
    if _productWords is not None and _productWords != '':
        condtions['comments__contains'] = _productWords
    if _productTime is not None and _productTime != '':
        condtions['commenttime__contains'] = _productTime
    if len(condtions) > 0:
        ret = TClnProductInfo.objects.values().filter(productcode__in=p_code_condition).filter(**condtions).iterator()
    else:
        ret = TClnProductInfo.objects.values().filter(productcode__in=p_code_condition).iterator()
    ret_list = list(ret)
    return JsonResponse({'ret_list':ret_list})