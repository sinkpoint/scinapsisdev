from django.shortcuts import render
from search.models import PubTechProdResult
from django.db.models import Count
from django.shortcuts import redirect

import logging

def _get_user_info(req):
    if req.user:
        return req.user
    else:
        return None

# Create your views here.
def _get_catids_from_q(query):
    if not query:
        return []

    from search.models import PubProductName
    from django.db.models import Q

    cat_ids = PubProductName.objects.filter(Q(name1__contains=query) | Q(name2__contains=query) |
        Q(name3__contains=query) | Q(name4__contains=query) | Q(name5__contains=query)).values('id')
    cat_ids = [ i['id'] for i in cat_ids]
    logging.warning(cat_ids)
    return cat_ids

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')

def login_view(request):
    user = _get_user_info(request)
    if user and not user.is_anonymous():
        return dashboard(request)

    else:
        from django.contrib.auth import authenticate, login

        if 'username' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dash')
                else:
                    # Return a 'disabled account' error message
                    pass
            else:
                # Return an 'invalid login' error message.
                pass

        from .forms import LoginForm
        login_form = LoginForm()

        return render(request,'login.html',{'user':user, 'form':login_form})


def _query_constructor(request):
    m_query = {}
    if 'query_set' in request.session:
        m_query = request.session['query_set']

    # get unique product ids that contains keyword search
    data = PubTechProdResult.objects.all()

    if 'q' in request.GET:
        m_query['q'] = request.GET['q']
        cat_ids = _get_catids_from_q(m_query['q'])
        if cat_ids:
            data = PubTechProdResult.objects.filter(prod_id__in=cat_ids)

    if 't' in request.GET:
        tech_name = request.GET['t']
        m_query['tech_name'] = tech_name
        data = data.filter(tech_parental_name=tech_name)

    return (m_query, data)


def dashboard(request):
    user = _get_user_info(request)
    if not user or user.is_anonymous():
        return redirect('login')

    pass_data = {'user': user}

    q_input, data = _query_constructor(request)
    pass_data['query_set'] = q_input
    request.session['query_set'] = q_input
    logging.warning(request.session['query_set'])
    tech_stats = data.values('tech_parental_name').annotate(Count('tech_parental_name')).order_by()

    data = []
    for i in tech_stats:
        ks = i.keys()
        data.append([str(i[ks[0]]),i[ks[1]]])

    pass_data['data'] = data
    pass_data['request'] = request.GET
    return render(request, "search/dashboard.html", pass_data)


def index(request):
    user = _get_user_info(request)
    if not user or user.is_anonymous():
        return redirect('login')

    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

    pass_data = {'user':user}

    q_input, data = _query_constructor(request)
    pass_data['query_set'] = q_input

    # data = data.values('figure__url', 'figure__header','figure__content',
    #     'doc__title', 'tech_parental_name', 'doc__publisher','doc__src_address',
    #     'doc__pdf_address','supplier', 'product_name').annotate(Count('figure__url')).order_by('doc__title', 'figure__figure_id')

    data = data.order_by('doc__title', 'figure__header')

    pagi = Paginator(data, 30)
    page = request.GET.get('page')
    try:
        pdata = pagi.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pdata = pagi.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pdata = pagi.page(pagi.num_pages)

    pass_data['data'] = pdata
    return render(request, "search/index.html", pass_data)