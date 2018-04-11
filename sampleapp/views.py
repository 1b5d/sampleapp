from django.views.generic import ListView, DetailView
from sampleapp.models import SampleSite


class SiteListView(ListView):
    model = SampleSite
    queryset = SampleSite.objects.order_by('id')
    template_name = 'site-list.html'


class SiteDetailView(DetailView):
    model = SampleSite
    template_name = 'site_detail.html'


class SummaryView(ListView):
    model = SampleSite
    queryset = SampleSite.objects.order_by('id')
    template_name = 'summary.html'

    def get_context_data(self, **kwargs):
        context = super(SummaryView, self).get_context_data(**kwargs)
        context['aggr_attr_a'] = 'sum_a'
        context['aggr_attr_b'] = 'sum_b'
        return context


class SummaryAverageView(ListView):
    model = SampleSite
    queryset = SampleSite.objects.order_by('id')
    template_name = 'summary.html'

    def get_context_data(self, **kwargs):
        context = super(SummaryAverageView, self).get_context_data(**kwargs)
        context['aggr_attr_a'] = 'avg_a'
        context['aggr_attr_b'] = 'avg_b'
        return context
