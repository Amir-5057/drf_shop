from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = models.TextField(_('description'))
    discount = models.IntegerField(_('discount'), default=0)
    price = models.IntegerField(_('price'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created at'))
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('category'))
    short_desc = models.TextField(verbose_name=_("short description"))

    view_count = models.IntegerField(_("view count"), default=0)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"),
                                on_delete=models.CASCADE,
                                related_name="product_images")
    image = models.ForeignKey('media.Media', verbose_name=_("image"),
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")

    def __str__(self):
        return f"Id: {self.id}| Product: {self.product.title}"


class Characteristic(models.Model):
    title = models.CharField(_("title"), max_length=100)
    product = models.ForeignKey(Product, verbose_name=_("product"),
                                on_delete=models.CASCADE,
                                related_name='characteristics')

    class Meta:
        verbose_name = _("Characteristic")
        verbose_name_plural = _("Characteristics")

    def __str__(self):
        return self.title


class CharacteristicValue(models.Model):
    title = models.CharField(_("title"), max_length=100)
    characteristic = models.ForeignKey(Characteristic,
                                       on_delete=models.CASCADE,
                                       related_name='values')

    class Meta:
        verbose_name = _("characteristic value")
        verbose_name_plural = _("characteristic values")

    def __str__(self):
        return self.title


class Instruction(models.Model):
    title = models.CharField(_("title"), max_length=100)
    desc = models.TextField(_("description"))
    left_image = models.ForeignKey("media.Media",
                                   verbose_name=_("left image"),
                                   on_delete=models.CASCADE,
                                   related_name="instructions_left_image")
    right_image = models.ForeignKey("media.Media",
                                    verbose_name=_("right image"),
                                    on_delete=models.CASCADE,
                                    related_name="instructions_right_image")

    product = models.ForeignKey(Product, verbose_name=_("product"),
                                on_delete=models.CASCADE,
                                related_name="instructions")

    class Meta:
        verbose_name = _("instruction")
        verbose_name_plural = _("instructions")

    def __str__(self):
        return self.title


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        NEW = 'New', _("new")
        ACCEPTED = 'Accepted', _("accepted")
        PROGRESS = 'Progress', _("progress")
        CANCELLED = 'Cancelled', _("cancelled")
        FINISHED = 'finished', _("finished")

    full_name = models.CharField(_("full name"), max_length=120)

    status = models.CharField(_("status"), max_length=20, choices=OrderStatus.choices,
                              default=OrderStatus.NEW)
    total_price = models.FloatField(_("total price"), default=0)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return self.full_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order"),
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("product"),
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quantity"), default=1)

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")
        unique_together = ['order', 'product']

    def __str__(self):
        return f"Id: {self.id}| Q: {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity
