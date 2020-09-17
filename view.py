from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
import io
import networkx as nx
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from .models import Player
from rest_framework import generics
from .serializers import PlayerSerializer
mpl.use('Agg')

count_player = 0  # 参加ユーザ数


def login():
    u


class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"


class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"


'''
class IndexView(TemplateView):
    template_name = "accounts/index.html"
'''


def index(request):
    if request.user.is_authenticated:
        print("index_authenticated")
    else:
        print("fail_index_authenticated")

    return render(request, "manager/top.html")


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/create.html"
    success_url = reverse_lazy("login")


class List_Player(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class One_Player(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


def entry(request):
    context = {
        'player_list': Player.objects.all()
    }
    return render(request, 'manager/entry.html', context=context)


def top(request):  # player_id
    if request.method == 'POST':
        if 'button_0' in request.POST:
            col_num = 0
            print(col_num)
        elif 'button_1' in request.POST:
            col_num = 1
            print(col_num)
        elif 'button_2' in request.POST:
            col_num = 2
            print(col_num)

        return render(request, 'manager/top.html')
    else:
        context = {
            'player_list': Player.objects.all()
        }
        return render(request, 'manager/top.html', context=context)


def ones_view(request):
    if request.method == 'POST':
        if 'button_0' in request.POST:
            col_num = 0
            print(col_num)
        elif 'button_1' in request.POST:
            col_num = 1
            print(col_num)
        elif 'button_2' in request.POST:
            col_num = 2
            print(col_num)

        return render(request, 'manager/ones_view.html')
    else:
        context = {
            # ＃nodenum = "ハッシュから持ってきたユーザの"
        }
    return render(request, 'manager/ones_view.html', context=content)

# matplotlibの出力をpngに変換


def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s


def make_network_graph(size):
    graph = np.zeros((size, size))
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if j > i:
                num = np.random.rand()
                if num < 0.25:
                    graph[i][j] = 0
                elif num >= 0.25 and num < 0.5:
                    graph[i][j] = 1
                elif num >= 0.5 and num < 0.75:
                    graph[i][j] = 2
                else:
                    graph[i][j] = 3
    return graph


def make_nodes(size):
    nodes = []
    for i in range(size):
        tmp = sum(graph[i])
        if int(tmp % 3) == 0:
            color = 'red'
        elif int(tmp % 3) == 1:
            color = 'blue'
        elif int(tmp % 3) == 2:
            color = 'green'
        nodes.append((i, {'color': color}))
    return nodes


def make_edges(nodes):
    edges = []
    for hi, hv in enumerate(graph):
        for wi, wv in enumerate(hv):
            if(wv):
                edges.append((nodes[hi][0], nodes[wi][0]))  # 隣接行列において2点間の値が真ならば、無向のエッジを追加
    return edges


def get_color_from_node(node_num):
    tmp = list(nodes[node_num])
    if tmp[1]['color'] == 'red':
        return 'red'
    elif tmp[1]['color'] == 'blue':
        return 'blue'
    elif tmp[1]['color'] == 'green':
        return 'green'


def get_color_from_db(node_num):
    p = Player.objects.get(pid=node_num)
    return p.color


def change_color(nodes, node_num, color):
    tmp = list(nodes[node_num])
    tmp[1] = {'color': color}
    node_changed = tuple(tmp)
    p = Player.objects.get(pid=node_num)
    p.color = color
    p.save()
    return node_changed


def search_neibor(i):
    neibor = []
    for j in range(len(graph[i])):
        if j > i:
            if graph[i][j] > 0:
                neibor.append(j)
        else:
            if graph[j][i] > 0:
                neibor.append(j)
    return neibor


def get_neibor_nodes(i):
    neibor_list = search_neibor(i)
    neibor_nodes = []
    for j in range(size):
        for k in range(len(neibor_list)):
            if nodes[j][0] == neibor_list[k]:
                neibor_nodes.append(nodes[j])
    return neibor_nodes


def make_linked_edges(i, neibor_nodes):
    linked_edges = []
    for j in range(len(neibor_nodes)):
        linked_edges.append((i, neibor_nodes[j][0]))
    return linked_edges


def make_neibor_network(neibor_nodes_all, linked_edges_all):
    for i in range(size):
        neibor_nodes_all.append(get_neibor_nodes(i))
        linked_edges_all.append(make_linked_edges(i, neibor_nodes_all[i]))


def draw_network(self):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    node_color = [node['color'] for node in G.nodes.values()]

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color=node_color)

    plt.axis("off")
    network_png = plt2png()
    plt.cla()

    response = HttpResponse(network_png, content_type='image/png')
    return response


def draw_my_network(self, pk):
    G = nx.Graph()
    G.add_nodes_from(neibor_nodes_all[pk])
    G.add_edges_from(linked_edges_all[pk])

    node_color = []
    for i in list(G):
        node_color.append(get_color_from_db(i))

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color=node_color)

    plt.axis("off")
    network_png = plt2png()
    plt.cla()

    response = HttpResponse(network_png, content_type='image/png')
    return response


def create_user(nodes):
    for i in range(size):
        Player(i, get_color_from_node(i)).save()


def use_player(pid):
    check = False
    while check == False:
        p = Player.objects.get(pid=pid)
        if p.use == False:
            check = True
            p.use = True
    p.save()


size = 7
player = np.zeros(size)
graph = make_network_graph(size)
nodes = make_nodes(size)
edges = make_edges(nodes)
neibor_nodes_all = []
linked_edges_all = []
create_user(nodes)
use_player(np.random.randint(0, size-1))
make_neibor_network(neibor_nodes_all, linked_edges_all)
