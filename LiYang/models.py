from django.db import models


class House(models.Model):
    '''
    这是房子的总类, 包括房子价格, 面积大小, 楼层, 布局, 地段
    '''
    name = models.CharField(verbose_name='开盘名称', max_length=80)
    price = models.CharField(verbose_name='价格', max_length=80)
    area = models.IntegerField(verbose_name='面积', unique=True)
    floor = models.IntegerField(verbose_name='所处楼层', )
    image = models.ImageField(verbose_name='图片信息',default=None)
    address = models.TextField(verbose_name='地址', )
    message = models.CharField(verbose_name='其他信息', max_length=80)
    create_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    def __str__(self):
        return self.name
