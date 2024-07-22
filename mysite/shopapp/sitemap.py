from django.contrib.sitemaps import Sitemap

from .models import Product


class ShopSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Product.objects.filter(creted_at__isnull=False).order_by('-creted_at')
    
    def lastmod(self, obj: Product):
        return obj.creted_at
