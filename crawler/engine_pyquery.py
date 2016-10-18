<!--Create a new Crawler to take on 'English' web site http://www.foodnetwork.com/recipes.html of recipes-->
from pyquery import PyQuery    
html = # Your HTML CODE
pq = PyQuery(html)
tag = pq('div#class')
print tag.text()


import os
import django
from collections import Counter
from .models import DataIngredient, DataWayCooking, IngredientSpec
from pyquery import PyQuery 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silverplate.settings")
django.setup()

   
html = # <html class="webkit"><head prefix="og: http://ogp.me/ns# video: http://ogp.me/ns/video#"><link type="text/css" rel="stylesheet" href="http://www.pdk.video.snidigital.com/5.6.12/pdk/style/default.css" media="screen"><script type="text/javascript" src="https://bam.nr-data.net/1/ca450cca9d?a=2623209&amp;v=995.3402600&amp;to=ZAYGMhNQDUQCAEILWl1MNgMQRAZEFyJCFkdaARESBB4QWQpOUA1aV0wHCQxBDFkGDUIRGkMCAwMVSBNSEExDDFxFBhYVAF1OWwINUgtbVA%3D%3D&amp;rst=45119&amp;ref=http://www.foodnetwork.com/recipes.html&amp;ap=521&amp;be=1592&amp;fe=40754&amp;dc=20415&amp;perf=%7B%22timing%22:%7B%22of%22:1476189793418,%22n%22:0,%22f%22:414,%22dn%22:414,%22dne%22:414,%22c%22:414,%22ce%22:414,%22rq%22:427,%22rp%22:802,%22rpe%22:2769,%22dl%22:818,%22di%22:22002,%22ds%22:22007,%22de%22:24510,%22dc%22:42344,%22l%22:42345,%22le%22:42415%7D,%22navigation%22:%7B%7D%7D&amp;jsonp=NREUM.setToken"></script><script src="https://js-agent.newrelic.com/nr-995.min.js"></script><script src="http://edge.quantserve.com/quant.js" async="" type="text/javascript"></script><script type="text/javascript" async="" src="//wsc3.webspectator.com/init?appId=41FC8862&amp;h=http%3A%2F%2Fwww.foodnetwork.com%2Frecipes.html&amp;t=1476189829696"></script><script src="http://pagead2.googlesyndication.com/pagead/osd.js"></script><script src="//pagead2.googlesyndication.com/pagead/expansion_embed.js?source=safeframe"></script><script type="text/javascript" async="" src="//assets.pinterest.com/js/pinit_main.js?0.24616943323590057"></script><script src="//tru.am/scripts/ta-pagesocial-sdk.js"></script><script async="" type="text/javascript" src="http://www.googletagservices.com/tag/js/gpt.js"></script><script type="text/javascript" async="" data-ev-tag-pid="1212" data-ev-tag-ocid="814" src="http://c.betrad.com/pub/tag.js"></script><script async="" src="http://b.scorecardresearch.com/beacon.js"></script><script charset="UTF-8" type="text/javascript" src="http://cdn.taboola.com/libtrc/impl.229-22-RELEASE.js"></script><script type="text/javascript" src="http://scripps.demdex.net/event?d_mid=90984221319115826754795320241096337862&amp;d_nsid=0&amp;d_ld=_ts%3D1476189805531&amp;d_rtbd=json&amp;d_jsonv=1&amp;d_dst=1&amp;d_cb=demdexRequestCallback_0_1476189805531&amp;c_pageName=%2Frecipes.html&amp;c_referrer=https%3A%2F%2Fwww.google.de%2F&amp;c_channel=recipes%20%26amp%3B%20how-tos&amp;c_events=event1&amp;c_prop5=recipes%20%26amp%3B%20how-tos&amp;c_prop6=recipes%20%26amp%3B%20how-tos&amp;c_prop8=recipes%2C%20food&amp;c_prop9=food%7Cuniversal-landing%7C4d24061e-a71e-4e63-b213-2938db662de7%7C1&amp;c_prop10=universal-landing&amp;c_prop13=New&amp;c_prop20=88948361278089666533763699047144264608&amp;c_prop33=Tue-8.5A&amp;c_eVar42=true&amp;c_prop53=food&amp;c_prop60=web&amp;c_eVar60=displayed&amp;c_prop62=FN%20CQ%2020160810&amp;c_prop67=2015-09-01%7C2016-09-16%7C%3E1%20year%7C8%20days-1%20month&amp;c_prop75=Logged%20Out&amp;c_contextData_eVar76=0%7C0%7C400%7C2000%7C-1%7C-1%7C-1%7C-1"></script><script type="text/javascript" async="async" src="http://sa.foodnetwork.com/id?d_visid_ver=1.5.3&amp;callback=s_c_il%5B0%5D._setAnalyticsFields&amp;mcorgid=BC501253513148ED0A490D45%40AdobeOrg&amp;mid=90984221319115826754795320241096337862"></script><script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script><script type="text/javascript" async="async" src="http://dpm.demdex.net/id?d_visid_ver=1.5.3&amp;d_rtbd=json&amp;d_ver=2&amp;d_verify=1&amp;d_orgid=BC501253513148ED0A490D45%40AdobeOrg&amp;d_nsid=0&amp;d_cb=s_c_il%5B0%5D._setMarketingCloudFields"></script>

    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>Food Network Recipes &amp; Easy Cooking Techniques</title>
    <meta name="description" content="Find 1000s of Food Network's best recipes from top chefs, shows and experts. And watch videos demonstrating recipe prep and cooking techniques.">
    
    

    
   	<meta property="fb:admins" content="7207947">
   	<meta property="fb:admins" content="16504712">
    <meta property="fb:app_id" content="283495858517689">

    <meta itemprop="og:headline" content="Food Network Recipes &amp; Easy Cooking Techniques">
<meta property="og:type" content="article">
<meta property="og:title" content="Food Network Recipes &amp; Easy Cooking Techniques">
<meta property="og:description" content="Find 1000s of Food Network&amp;apos;s best recipes from top chefs, shows and experts. And watch videos demonstrating recipe prep and cooking techniques.">
<meta itemprop="og:description" content="Find 1000s of Food Network&amp;apos;s best recipes from top chefs, shows and experts. And watch videos demonstrating recipe prep and cooking techniques.">
<meta property="sailthru.tags" content="recipes">
<meta property="og:url" content="http://www.foodnetwork.com/recipes.html">
<meta property="og:image" content="http://foodnetwork.sndimg.com/content/dam/images/food/fullset/2009/4/15/0/NY0409-1_Sweet-Cola-Ribs_s4x3.jpg.rend.sniipadlarge.jpeg">

    






    
<script async="" type="text/javascript" src="http://native.sharethrough.com/assets/sfp.js"></script><script async="" src="http://cdn.taboola.com/libtrc/foodnetwork/loader.js"></script><script id="facebook-jssdk" src="//connect.facebook.net/en_US/all.js#xfbml=1&amp;appId=283495858517689"></script><script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,t,n){function r(n){if(!t[n]){var o=t[n]={exports:{}};e[n][0].call(o.exports,function(t){var o=e[n][1][t];return r(o||t)},o,o.exports)}return t[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(e,t,n){function r(){}function o(e,t,n){return function(){return i(e,[(new Date).getTime()].concat(u(arguments)),t?null:this,n),t?void 0:this}}var i=e("handle"),a=e(2),u=e(3),c=e("ee").get("tracer"),f=NREUM;"undefined"==typeof window.newrelic&&(newrelic=f);var s=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit"],l="api-",p=l+"ixn-";a(s,function(e,t){f[t]=o(l+t,!0,"api")}),f.addPageAction=o(l+"addPageAction",!0),f.setCurrentRouteName=o(l+"routeName",!0),t.exports=newrelic,f.interaction=function(){return(new r).get()};var d=r.prototype={createTracer:function(e,t){var n={},r=this,o="function"==typeof t;return i(p+"tracer",[Date.now(),e,n],r),function(){if(c.emit((o?"":"no-")+"fn-start",[Date.now(),r,o],n),o)try{return t.apply(this,arguments)}finally{c.emit("fn-end",[Date.now()],n)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,t){d[t]=o(p+t)}),newrelic.noticeError=function(e){"string"==typeof e&&(e=new Error(e)),i("err",[e,(new Date).getTime()])}},{}],2:[function(e,t,n){function r(e,t){var n=[],r="",i=0;for(r in e)o.call(e,r)&&(n[i]=t(r,e[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;t.exports=r},{}],3:[function(e,t,n){function r(e,t,n){t||(t=0),"undefined"==typeof n&&(n=e?e.length:0);for(var r=-1,o=n-t||0,i=Array(o<0?0:o);++r<o;)i[r]=e[t+r];return i}t.exports=r},{}],ee:[function(e,t,n){function r(){}function o(e){function t(e){return e&&e instanceof r?e:e?c(e,u,i):i()}function n(n,r,o){if(!d){e&&e(n,r,o);for(var i=t(o),a=v(n),u=a.length,c=0;c<u;c++)a[c].apply(i,r);var f=s[y[n]];return f&&f.push([b,n,r,i]),i}}function p(e,t){w[e]=v(e).concat(t)}function v(e){return w[e]||[]}function g(e){return l[e]=l[e]||o(n)}function m(e,t){f(e,function(e,n){t=t||"feature",y[n]=t,t in s||(s[t]=[])})}var w={},y={},b={on:p,emit:n,get:g,listeners:v,context:t,buffer:m,abort:a};return b}function i(){return new r}function a(){d=!0,s=p.backlog={}}var u="nr@context",c=e("gos"),f=e(2),s={},l={},p=t.exports=o(),d=!1;p.backlog=s},{}],gos:[function(e,t,n){function r(e,t,n){if(o.call(e,t))return e[t];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[t]=r,r}var o=Object.prototype.hasOwnProperty;t.exports=r},{}],handle:[function(e,t,n){function r(e,t,n,r){o.buffer([e],r),o.emit(e,t,n)}var o=e("ee").get("handle");t.exports=r,r.ee=o},{}],id:[function(e,t,n){function r(e){var t=typeof e;return!e||"object"!==t&&"function"!==t?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");t.exports=r},{}],loader:[function(e,t,n){function r(){if(!h++){var e=b.info=NREUM.info,t=l.getElementsByTagName("script")[0];if(setTimeout(f.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&t))return f.abort();c(w,function(t,n){e[t]||(e[t]=n)}),u("mark",["onload",a()],null,"api");var n=l.createElement("script");n.src="https://"+e.agent,t.parentNode.insertBefore(n,t)}}function o(){"complete"===l.readyState&&i()}function i(){u("mark",["domContent",a()],null,"api")}function a(){return(new Date).getTime()}var u=e("handle"),c=e(2),f=e("ee"),s=window,l=s.document,p="addEventListener",d="attachEvent",v=s.XMLHttpRequest,g=v&&v.prototype;NREUM.o={ST:setTimeout,CT:clearTimeout,XHR:v,REQ:s.Request,EV:s.Event,PR:s.Promise,MO:s.MutationObserver},e(1);var m=""+location,w={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-995.min.js"},y=v&&g&&g[p]&&!/CriOS/.test(navigator.userAgent),b=t.exports={offset:a(),origin:m,features:{},xhrWrappable:y};l[p]?(l[p]("DOMContentLoaded",i,!1),s[p]("load",r,!1)):(l[d]("onreadystatechange",o),s[d]("onload",r)),u("mark",["firstbyte",a()],null,"api");var h=0},{}]},{},["loader"]);</script>

    
    





	
	




<link rel="canonical" href="http://www.foodnetwork.com/recipes.html"> 






    
    

<script>
    (function (console) {

        var isDebug, debugFlag, fakeConsole, noop, methods;

        function persistDebugFlag(flag) {
            if (typeof flag !== 'undefined') {
                document.cookie = 'persistDebugFlag=' + !!flag;
            }

            return document.cookie.indexOf('persistDebugFlag=true') !== -1;
        }


        isDebug = persistDebugFlag();
        debugFlag = 'debug=';

        if (window.location && window.location.search) {

            if (window.location.search.indexOf(debugFlag + 'false') !== -1) {
                isDebug = false;

                persistDebugFlag(false);

            } else if (window.location.search.indexOf(debugFlag + 'true') !== -1) {
                isDebug = true;

                persistDebugFlag(true);
            }
        }

        if (!isDebug) {
            // Avoid possible security complains
            try {

                noop = function () {
                };

                fakeConsole = {};

                methods = ['assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error', 'exception', 'group', 'groupCollapsed',
                    'groupEnd', 'info', 'log', 'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
                    'timeStamp', 'trace', 'warn'];

                methods.map(function (method) {
                    fakeConsole[method] = noop;
                });

                console.log("Console logging has been disabled on this site. Please set the debug flag in the URL to view log messages.");
                window.console = fakeConsole;
            }
            catch (e) {
                console.warn('Attempt to suppress the console failed: %s', e.message);
            }
        }
    })(window.console);
</script>
<script type="text/javascript">
    if (typeof AUT === "undefined") { AUT = {}; AUT.jserrors = []; }
    window.onerror = function(message, url, linenumber){
        AUT.jserrors.push({ 'message': message, 'url': url, 'linenumber': linenumber });
    };
</script>


    

  <link rel="stylesheet" type="text/css" href="http://fn-static.sndimg.com/prod/community/css/fn-community.css">

    <script src="http://js.indexww.com/ht/ls-scripps.js"></script>

    


    <!--[NON IE8] -->
    <!--[if gt IE 8]><!-->	
    	<link rel="stylesheet" href="/etc/designs/food/clientlib.min.css" type="text/css">

    <!--<![endif]-->
    <!--end non ie8-->

<!--[ALL] Config js used by all browsers -->
	<script type="text/javascript" src="/etc/designs/food/config.js"></script>
<!--end all-->

        <!--[ONLY IE8] -->
        <!-- IE8 specific css && IE8 specific js -->
        <!--[if lt IE 9]>
            <link rel="stylesheet" href="/etc/designs/food/clientlib-ie8.min.css" type="text/css">

            <script type="text/javascript" src="/etc/clientlibs/granite/jquery.min.js"></script>
<script type="text/javascript" src="/etc/clientlibs/granite/utils.min.js"></script>
<script type="text/javascript" src="/etc/clientlibs/granite/jquery/granite.min.js"></script>
<script type="text/javascript" src="/etc/clientlibs/foundation/jquery.min.js"></script>

            <script type="text/javascript" src="/etc/designs/food/clientlib-ie8/ie8-js/html5shiv-printshiv.js"></script>
            <script type="text/javascript" src="/etc/designs/food/clientlib-ie8.min.js"></script>

        <![endif]-->
        <!--end only ie8 -->


<!--[ALL] Main js used by all browsers -->
	<script type="text/javascript" src="/etc/designs/food/clientlib.min.js"></script><style></style>

<!--end all-->






	
	<script type="text/javascript">
		window._taboola = window._taboola || [];
		_taboola.push({
			category: 'auto',tracking:'ic1=tbla'
		});
		! function (e, f, u) {
			e.async = 1;
			e.src = u;
			f.parentNode.insertBefore(e, f);
		}(document.createElement('script'), document.getElementsByTagName('script')[0], 'http://cdn.taboola.com/libtrc/foodnetwork/loader.js');
	</script>



	<script type="text/javascript" src="http://dje7rr2pnbe7f.cloudfront.net/public/j/food-network/box-loader.js"></script>
  <!--pagetype: universal-landing-->
  
	<script id="fn-community-init" type="text/javascript" src="http://fn-static.sndimg.com/prod/community/js/fn-community-init.js" inclmustache="false" webloginui="true" communityapikey="3_ClDcX23A7tU8pcydnKyENXSYP5kxCbwH4ZO741ZOujPRY8Ksj2UBnj8Zopb0OX0K" moderateuserprofileurl="https://api.food.com/external/web/fn/moderateUserProfile" inclsocialupload="false" moderatecommenturl="https://api.food.com/external/web/fn/moderateComment" socialuploadurl="http://statics.scrippsnetworks.com/wrapper/js/socialupload_widget.min.js" socialuploadapikey="AsMMFcUZiTt2VBZByq8htz"></script><script src="https://cdns.gigya.com/JS/socialize.js?apikey=3_ClDcX23A7tU8pcydnKyENXSYP5kxCbwH4ZO741ZOujPRY8Ksj2UBnj8Zopb0OX0K"></script>
    <!--TEST-->
    

    <!--TEST-->


    
    <link rel="icon" type="image/vnd.microsoft.icon" href="/etc/designs/food/clientlib/img/favicon.ico">
    <link rel="shortcut icon" type="image/vnd.microsoft.icon" href="/etc/designs/food/clientlib/img/favicon.ico">
    
	
	  <script type="text/javascript" src="http://code.adsales.snidigital.com/conf/ads-config.min.js"></script>
		<script type="text/javascript" src="http://code.adsales.snidigital.com/lib/2/sni-ads.min.js"></script>
	
    <link href="https://plus.google.com/100091697767366769792" rel="publisher">
    

<script type="text/javascript">
    if (typeof MetaDataManager != "undefined") {
    	var mdManager = new MetaDataManager();
        var mdProps = {"AllTags":"","Delivery_Channel":"web","Sponsorship":"","UniqueID":"food|universal-landing|4d24061e-a71e-4e63-b213-2938db662de7|1","Type":"universal-landing","talentName":"","CategoryDspName":"recipes &amp; how-tos","DetailId":"4d24061e-a71e-4e63-b213-2938db662de7","Site":"food","CanonicalUrl":"http://www.foodnetwork.com/recipes.html","Restricted":"false","ImgURL":"http://foodnetwork.sndimg.com/content/dam/images/food/fullset/2009/4/15/0/NY0409-1_Sweet-Cola-Ribs_s4x3.jpg","Section":"recipes","Url":"/recipes.html","SctnDspName":"recipes &amp; how-tos","OrigPubDate":"2015-09-01T00:07:34.496-04:00|2016-09-16T15:38:48.178-04:00","Title":"recipes &amp; how-tos","Classification":"recipes, food","HubPath":"unknown","PageNumber":"1","HubSponsor":""};
    	for (var key in mdProps) {
            mdManager.addAttribute(key, mdProps[key]);
    	}
    }
</script>






<script type="text/javascript">
    if (typeof mdManager != "undefined") {
        mdManager.addParameter('UserId', typeof userIdCookieUserId != "undefined" ? userIdCookieUserId : '');
        mdManager.addParameter('UserIdEmail', typeof userIdEmail != "undefined" ? userIdEmail : '');
        mdManager.addParameter('UserIdCreateDt', typeof userIdCookieCreateDt != "undefined" ? userIdCookieCreateDt : '');
        mdManager.addParameter('UserIdVersion',  typeof userIdCookieVersion != "undefined" ? userIdCookieVersion : '');
    }
</script>

<script type="text/javascript">
    if (typeof AdManager != "undefined") {
		var adManager = new AdManager();
        initAdManager(adManager, mdManager);
    }
</script>
    

<!-- Dynamic Tag Manager Header. see cloudservicesconfig at /content/food/jcr:content  -->
pq = PyQuery(html)
<!--tag = pq('div#class')-->

tag = pq('div#ZN_0HYiPaKIOaocqih')
tag1 = pq('div#fb-root')
tag2 = pq('div#leaderboard_fixed')
tag3 = pq('div#leaderboard')
tag4 = pq('div#dfp_pushdown_brandscape')
tag5 = pq('div#brandscape')
tag6 = pq('div#fb-root.fb_reset')<!-- the dot here is div class-->
tag7 = pq('div#fb-dfp_utility1')
tag8 = pq('div#fb-dfp_utility2')
tag9 = pq('div#ws_inst_trigger')
tags = tag +tag1+tag2+tag3+tag4+tag5+tag5+tag6+tag7
print tags.text()


