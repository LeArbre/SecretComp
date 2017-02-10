# 项目说明
### [天池竞赛](https://tianchi.shuju.aliyun.com/competition/introduction.htm?spm=5176.100065.200879.2.OexTfv&raceId=231591)
### 重要时间
>2月8日  08:00: 评测启动  
3月7日  10:00: 报名截止&队伍融合截止  
3月8日  16:00: 更新评测集  
3月14日 16:00: 最后一次评测触发  & 比赛结束  
3月19日 23:59: 代码 & 解题思路提交截止  
3月24日 10:00: 获胜队伍公布  

### 数据说明
#### 数据时间段的问题
user_pay  时间范围是2015-06-26 06:00:00   2016-10-31 23:00:00。   
user_view 时间范围是2016-06-22 00:00:00   2016-10-31 23:00:00。    
extra_user_view  是2016-02-01 00:00:00   2016-06-21 23:00:00。    
user_pay表中，存在某些商家在某一时间区间内没有用户支付行为的情况。  
这是由于该商家在该时间段因某些原因没有正常经营导致的。  

#### 数据的详细描述
user_pay 是用户线下（非外卖消费，是到店消费）前往口碑店铺使用支付宝进行消费的记录。  
user_view 是用户线上在口碑平台浏览商家产生的记录。浏览行为指点击进入商家详情页浏览的行为。  
shop_info中，处于同一个location_id的商家相互距离小于2km，而且location_id本身没有实际意义。  
shop_level是口碑平台对商家规模的一个评价指标，例如个体餐饮商家的门店等级低于大型全国连锁的商家。   

#### 1. shop_info：商家特征数据
<table style="margin-left: 7px;background: rgb(208, 221, 239);border: none" width="418" border="1">
    <tbody>
        <tr style=";height:18px">
            <td style="width: 124px;border-width: 1px;border-color: black;background: transparent;padding: 5px;height: 18px" width="93">
                <p style="text-align:left">
                    <strong><span style="font-size:15px;font-family:'Microsoft YaHei'">Field</span></strong>
                </p>
            </td>
            <td style="width: 85px;border-top-width: 1px;border-right-width: 1px;border-bottom-width: 1px;border-top-color: black;border-right-color: black;border-bottom-color: black;border-left: none;background: transparent;padding: 5px;height: 18px" width="64">
                <p style="text-align:left">
                    <strong><span style="font-size:13px;font-family:'Microsoft YaHei'">Sample</span></strong>
                </p>
            </td>
            <td style="width: 348px;border-top-width: 1px;border-right-width: 1px;border-bottom-width: 1px;border-top-color: black;border-right-color: black;border-bottom-color: black;border-left: none;background: transparent;padding: 5px;height: 18px" width="261">
                <p style="text-align:left">
                    <strong><span style="font-size:15px;font-family:'Microsoft YaHei'">Description</span></strong>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">shop_id</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">000001</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p>
                    <span style="font-family:'Microsoft YaHei'">商家</span><span style="font-family:'Microsoft YaHei'">id</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">city_name</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-family:'Microsoft YaHei'">北京</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">市名</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">location_id</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">001</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">所在位置编号，位置接近的商家具有相同的编号</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">per_pay</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">3</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">人均消费（</span><span style="font-size:15px;font-family:'Microsoft YaHei'">数值越大消费越高</span><span style="font-size:15px;font-family:   'Microsoft YaHei'">）</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">score</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">1</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">评分</span><span style="font-size:15px;font-family:'Microsoft YaHei'">（数值越大评分越高）</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">comment_cnt</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">2</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">评论数</span><span style="font-size:15px;font-family:'Microsoft YaHei'">（数值越大评论数越多）</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">shop_level</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">1</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">门店等级</span><span style="font-size:15px;font-family:'Microsoft YaHei'">（数值越大门店等级越高）</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">cate_1_name</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">美食</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">一级品类名称</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">cate_2_name</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">小吃</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">二级分类名称</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">cate_3_name</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">其他小吃</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">三级分类名称</span>
                </p>
            </td>
        </tr>
    </tbody>
</table>

#### 2. user_pay：用户支付行为
<table style="margin-left: 7px;background: rgb(208, 221, 239);border: none" width="418" border="1">
    <tbody>
        <tr style=";height:18px">
            <td style="width: 146px;border-width: 1px;border-color: black;background: transparent;padding: 5px;height: 18px" width="110">
                <p style="text-align:left">
                    <strong><span style="font-size:15px;font-family:'Microsoft YaHei'">Field</span></strong>
                </p>
            </td>
            <td style="width: 165px;border-top-width: 1px;border-right-width: 1px;border-bottom-width: 1px;border-top-color: black;border-right-color: black;border-bottom-color: black;border-left: none;background: transparent;padding: 5px;height: 18px" width="124">
                <p style="text-align:left">
                    <strong><span style="font-size:15px;font-family:'Microsoft YaHei'">Sample</span></strong>
                </p>
            </td>
            <td style="width: 246px;border-top-width: 1px;border-right-width: 1px;border-bottom-width: 1px;border-top-color: black;border-right-color: black;border-bottom-color: black;border-left: none;background: transparent;padding: 5px;height: 18px" width="184">
                <p style="text-align:left">
                    <strong><span style="font-size:15px;font-family:'Microsoft YaHei'">Description</span></strong>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 146px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="110">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">user_id</span>
                </p>
            </td>
            <td style="width: 165px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="124">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">0000000001</span>
                </p>
            </td>
            <td style="width: 246px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="184">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">用户</span><span style="font-size:15px;font-family:'Microsoft YaHei'">id</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 146px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="110">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">shop_id</span>
                </p>
            </td>
            <td style="width: 165px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="124">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">000001</span>
                </p>
            </td>
            <td style="width: 246px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="184">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">商家</span><span style="font-size:15px;font-family:'Microsoft YaHei'">id</span><span style="font-size:15px;font-family:'Microsoft YaHei'">，与</span><span style="font-size:15px;font-family:'Microsoft YaHei'">shop_info</span><span style="font-size:15px;font-family:'Microsoft YaHei'">对应</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 146px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="110">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">time_stamp</span>
                </p>
            </td>
            <td style="width: 165px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="124">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">2015-10-10 11:00:00</span>
                </p>
            </td>
            <td style="width: 246px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="184">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">支付时间</span>
                </p>
            </td>
        </tr>
    </tbody>
</table>
#### 3. user_view：用户浏览行为 
<table style="margin-left: 7px;background: rgb(208, 221, 239);border: none" width="418" border="1">
    <tbody>
        <tr style=";height:18px">
            <td style="width: 146px;border-width: 1px;border-color: black;background: transparent;padding: 5px;height: 18px" width="110">
                <p style="text-align:left">
                    <strong><span style="font-size:15px;font-family:'Microsoft YaHei'">Field</span></strong>
                </p>
            </td>
            <td style="width: 165px;border-top-width: 1px;border-right-width: 1px;border-bottom-width: 1px;border-top-color: black;border-right-color: black;border-bottom-color: black;border-left: none;background: transparent;padding: 5px;height: 18px" width="124">
                <p style="text-align:left">
                    <strong><span style="font-size:15px;font-family:'Microsoft YaHei'">Sample</span></strong>
                </p>
            </td>
            <td style="width: 246px;border-top-width: 1px;border-right-width: 1px;border-bottom-width: 1px;border-top-color: black;border-right-color: black;border-bottom-color: black;border-left: none;background: transparent;padding: 5px;height: 18px" width="184">
                <p style="text-align:left">
                    <strong><span style="font-size:15px;font-family:'Microsoft YaHei'">Description</span></strong>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 146px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="110">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">user_id</span>
                </p>
            </td>
            <td style="width: 165px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="124">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">0000000001</span>
                </p>
            </td>
            <td style="width: 246px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="184">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">用户</span><span style="font-size:15px;font-family:'Microsoft YaHei'">id</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 146px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="110">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">shop_id</span>
                </p>
            </td>
            <td style="width: 165px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="124">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">000001</span>
                </p>
            </td>
            <td style="width: 246px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="184">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">商家</span><span style="font-size:15px;font-family:'Microsoft YaHei'">id</span><span style="font-size:15px;font-family:'Microsoft YaHei'">，与</span><span style="font-size:15px;font-family:'Microsoft YaHei'">shop_info</span><span style="font-size:15px;font-family:'Microsoft YaHei'">对应</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 146px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="110">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">time_stamp</span>
                </p>
            </td>
            <td style="width: 165px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="124">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">2015-10-10 10:00:00</span>
                </p>
            </td>
            <td style="width: 246px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="184">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">浏览时间</span>
                </p>
            </td>
        </tr>
    </tbody>
</table>

#### 4. prediction：测试集与提交格式
<table style="margin-left: 7px;background: rgb(208, 221, 239);border: none" width="418" border="1">
    <tbody>
        <tr style=";height:18px">
            <td style="width: 124px;border-width: 1px;border-color: black;background: transparent;padding: 5px;height: 18px" width="93">
                <p style="text-align:left">
                    <strong><span style="font-size:15px;font-family:'Microsoft YaHei'">Field</span></strong>
                </p>
            </td>
            <td style="width: 85px;border-top-width: 1px;border-right-width: 1px;border-bottom-width: 1px;border-top-color: black;border-right-color: black;border-bottom-color: black;border-left: none;background: transparent;padding: 5px;height: 18px" width="64">
                <p style="text-align:left">
                    <strong><span style="font-size:13px;font-family:'Microsoft YaHei'">Sample</span></strong>
                </p>
            </td>
            <td style="width: 348px;border-top-width: 1px;border-right-width: 1px;border-bottom-width: 1px;border-top-color: black;border-right-color: black;border-bottom-color: black;border-left: none;background: transparent;padding: 5px;height: 18px" width="261">
                <p style="text-align:left">
                    <strong><span style="font-size:15px;font-family:'Microsoft YaHei'">Description</span></strong>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">shop_id</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">000001</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">商家</span><span style="font-size:15px;font-family:'Microsoft YaHei'">id</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">day_1</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">25</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">第</span><span style="font-size:15px;font-family:'Microsoft YaHei'">1</span><span style="font-size:15px;font-family:'Microsoft YaHei'">天的预测值（ 需要选手提供）</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">day_2</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">3</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">第</span><span style="font-size:15px;font-family:'Microsoft YaHei'">2</span><span style="font-size:15px;font-family:'Microsoft YaHei'">天的预测值（需要选手提供）</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">……</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">&nbsp;</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">&nbsp;</span>
                </p>
            </td>
        </tr>
        <tr style=";height:22px">
            <td style="width: 124px;border-right-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-color: black;border-bottom-color: black;border-left-color: black;border-top: none;background: transparent;padding: 5px;height: 22px" width="93">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">day_14</span>
                </p>
            </td>
            <td style="width: 85px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="64">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">1024</span>
                </p>
            </td>
            <td style="width: 348px;border-top: none;border-left: none;border-bottom-width: 1px;border-bottom-color: black;border-right-width: 1px;border-right-color: black;background: transparent;padding: 5px;height: 22px" width="261">
                <p style="text-align:left">
                    <span style="font-size:15px;font-family:'Microsoft YaHei'">第</span><span style="font-size:15px;font-family:'Microsoft YaHei'">14</span><span style="font-size:15px;font-family:'Microsoft YaHei'">天的预测值（ 需要选手提供）</span>
                </p>
            </td>
        </tr>
    </tbody>
</table>
