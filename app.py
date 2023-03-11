import json
from collections import OrderedDict
#---------------------------------
# kalkicode.com 
# These methods have not been changed by our tools.
# ob_start
# curl_init
# curl_setopt
# curl_exec
# curl_error
# file_get_contents
# jdate
# mkdir
# Source_Home
# in_array
# file_put_contents
# strpos
# str_replace
# mt_rand
# getUserProfilePhotos
# unlink
# feof
# fgets
# Forward
#----------------------------


#---------------------------------
# kalkicode.com (Useful modifier code that might be useful to you).
"""
# open file with read mod
file = open('location/file.txt', 'r')
# reading text file data of line by line 
for data in file:
    print (data)
"""
#----------------------------

#
#تمامی حقوق کد نویسی و انتشار این ربات برای سایت نازروید محفوظ است 
#WWW.NAZROID.IR
#

ob_start();
include 'jdf.php';
API_KEY = '5869860329:AAFr7MTDSpIRpUWBtZDNXT_ZlqWCA3tRjmo';
# توکن ربات را در اینجا قرار دهید
#WWW.NAZROID.IR//
def Source_Home(method, datas = OrderedDict([])) :

    url = str(str("https://api.telegram.org/bot" + str(API_KEY)) + "/") + str(method);
    ch = curl_init();
    curl_setopt(ch, CURLOPT_URL, url);
    curl_setopt(ch, CURLOPT_RETURNTRANSFER, True);
    curl_setopt(ch, CURLOPT_POSTFIELDS, datas);
    res = curl_exec(ch);
    if (curl_error(ch)) :
        print(curl_error(ch));
    else : 
        return OrderedDict(json.loads(res));
    

#WWW.NAZROID.IR//
Dev = OrderedDict([(0,"232531269"),(1,"0000"),(2,"0000")]);
# آیدی های ادمین ها را در اینجا قرار دهید
usernamebot = "alibaratikonkourbot";
# آیدی ربات را در اینجا بدون @ قرار دهید
channel = "alibaratikonkour";
# آیدی کانال را در اینجا بدون @ قرار دهید
token = API_KEY;
# در اینجا چیزی رو دست نزنید
poshtibani = "nazroid1";
# آیدی مستقیم پشتیبانی را بدون @ در اینجا قرار دهید
botsupport = "nazroid1";
# آیدی پشتیبانی برای افراد ریپورت را بدون @ در اینجا قرار دهید
#WWW.NAZROID.IR//
update = OrderedDict(json.loads(file_get_contents('php://input')));
message = update.message;
from_id = message.from.id;
chat_id = message.chat.id;
message_id = message.message_id;
first_name = message.from.first_name;
last_name = message.from.last_name;
username = message.from.username;
Source_Home = message.text;
firstname = update.callback_query.from.first_name;
usernames = update.callback_query.from.username;
chatid = update.callback_query.message.chat.id;
fromid = update.callback_query.from.id;
membercall = update.callback_query.id;
time = jdate('H:i:s');
date = jdate("Y/F/d");
#WWW.NAZROID.IR//
forward_from_chat = update.message.forward_from_chat;
from_chat_id = forward_from_chat.id;
data = update.callback_query.data;
messageid = update.callback_query.message.message_id;
tc = update.message.chat.type;
gpname = update.callback_query.message.chat.title;
namegroup = update.message.chat.title;
forward_from = update.message.forward_from;
forward_from_id = forward_from.id;
forward_from_username = forward_from.username;
reply = update.message.reply_to_message.forward_from.id;
#WWW.NAZROID.IR//
forchannel = OrderedDict(json.loads(file_get_contents(str(str(str(str("https://api.telegram.org/bot" + str(token)) + "/getChatMember?chat_id=@") + str(channel)) + "&user_id=") + str(from_id))));
tch = forchannel.result.status;
forchannelq = OrderedDict(json.loads(file_get_contents(str(str(str(str("https://api.telegram.org/bot" + str(token)) + "/getChatMember?chat_id=@") + str(channel)) + "&user_id=") + str(fromid))));
tchq = forchannelq.result.status;
#WWW.NAZROID.IR//
mkdir("data/" + str(from_id) + "");
@(select = file_get_contents("data/" + str(from_id) + "/select.txt"));
@(chat = file_get_contents("data/" + str(from_id) + "/chat.txt"));
@(member = file_get_contents('data/chat.txt'));
@(nashnas = file_get_contents("data/" + str(from_id) + "/nashnas.txt"));
@(nashnas2 = file_get_contents("data/" + str(fromid) + "/nashnas.txt"));
@(jenstyat = file_get_contents("data/" + str(from_id) + "/jenstyat.txt"));
@(age = file_get_contents("data/" + str(from_id) + "/age.txt"));
@(city = file_get_contents("data/" + str(from_id) + "/city.txt"));
@(adds = file_get_contents("data/" + str(from_id) + "/member.txt"));
@(adds2 = file_get_contents("data/" + str(fromid) + "/member.txt"));
@(numchat = file_get_contents("data/" + str(from_id) + "/numchat.txt"));
@(step = file_get_contents("data/" + str(from_id) + "/file.txt"));
@(vip = file_get_contents("data/" + str(from_id) + "/vip.txt"));
@(editinfo = file_get_contents("data/" + str(from_id) + "/edit.txt"));
@(name = file_get_contents("data/" + str(from_id) + "/name.txt"));
@(blocklist = file_get_contents('data/blocklist.txt'));
@(like = file_get_contents("data/" + str(from_id) + "/like.txt"));
@(deslike = file_get_contents("data/" + str(from_id) + "/deslike.txt"));
@(blacklist = file_get_contents("data/" + str(from_id) + "/blacklist.txt"));
@(frinds = file_get_contents("data/" + str(from_id) + "/frinds.txt"));
#WWW.NAZROID.IR//
def SendMessage(chat_id, text) :

    Source_Home('sendMessage', OrderedDict([('chat_id',chat_id),('text',text),('parse_mode','MarkDown')]));

def Forward(berekoja, azchejaei, kodompayam) :

    Source_Home('ForwardMessage', OrderedDict([('chat_id',berekoja),('from_chat_id',azchejaei),('message_id',kodompayam)]));

def getUserProfilePhotos(token, from_id) :

    url = str(str('https://api.telegram.org/bot' + str(token)) + '/getUserProfilePhotos?user_id=') + str(from_id);
    result = file_get_contents(url);
    result = OrderedDict(json.loads(result));
    result = result.result;
    return result;

#WWW.NAZROID.IR//
@(user = file_get_contents('Member.txt'));
members = user.split("\n");
if (not in_array(chat_id, members)) :
    add_user = file_get_contents('Member.txt');
    add_user += str(chat_id) + "\n";
    file_put_contents('Member.txt', add_user);

#WWW.NAZROID.IR//
if (strpos(blocklist, "" + str(from_id) + "") != False) :
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"🛑شما به خاطر رعایت نکردن قوانین از ربات مسدود شدید \n\n❇️لطفا پیام دوباره ارسال نکنید"),('reply_markup',json.dumps(OrderedDict([('KeyboardRemove',OrderedDict([])),('remove_keyboard',True)])))]));

if (strpos(Source_Home, '/start ') != False) :
    start = str_replace("/start ", "", Source_Home);
    if (start == from_id) :
        Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"شما قبلا به ربات دعوت شده ایده ✔️")]));
    else : 
        if (tch == 'member' or tch == 'creator' or tch == 'administrator') :
            if (start > 0) :
                file_put_contents("data/" + str(from_id) + "/numchat.txt", "10");
                file_put_contents("data/" + str(from_id) + "/member.txt", "0");
                file_put_contents("data/" + str(from_id) + "/like.txt", "0");
                file_put_contents("data/" + str(from_id) + "/deslike.txt", "0");
                adds1 = file_get_contents("data/" + str(start) + "/member.txt");
                newmember = adds1 + 1;
                file_put_contents("data/" + str(start) + "/member.txt", "" + str(newmember) + "");
                adds2 = file_get_contents("data/" + str(start) + "/member.txt");
                Source_Home('sendmessage', OrderedDict([('chat_id',start),('text',"یک کابر با لینک دعوت شما وارد ربات شد ✔️\n📌 تعداد افرادی که دعوت کرده اید : " + str(adds2) + "")]));
                Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"سلام دوست گرامی به ربات جایزه بگیر تیم نازروید خوش اومدی میتونی با دعوت دوستات به این ربات از جوایز ویژه ما بهرهمند بشی\n  \n\n📣 جوایز ویژه هفتگی🙈\n\n📣 جوایز ویژه هفتگی🙈\n\n🌿 جوایز خاص فقط برای شما👇\n\n\n📅 " + str(date) + "\n🕗 " + str(time) + "\n🤖 " + str(usernamebot) + "")]));
                file_put_contents("data/" + str(from_id) + "/name.txt", "" + str(first_name) + "");
            
        else : 
            Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"دوست گرامی " + str(first_name) + " عزیز شما در کانال پشتیبانی عضو نیستید و امکان استفاده از چت ناشناس را ندارید ⚠️\n\t\n⭕️برای استفاده کامل از ربات بایستی ابتدا در کانال زیر عضو شوید :\n\n🆔 @" + str(channel) + "\n\nسپس به ربات برگشته و مجدد دستور /start را ارسال کنید و امتحان کنید ✔️\n📅 " + str(date) + "\n🕗 " + str(time) + "\n🤖 " + str(usernamebot) + ""),('reply_markup',json.dumps(OrderedDict([('inline_keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"📍 عضویت در کانال"),('url',"https://t.me/" + str(channel) + "")]))])),(1,OrderedDict([(0,OrderedDict([('text',"📣 بررسی عضویت"),('callback_data',"lockchannel")]))]))]))])))]));
            file_put_contents("data/" + str(from_id) + "/inviter.txt", "" + str(start) + "");
        
    

if (Source_Home == "/start" and tc == "private") :
    if (strpos(user, "" + str(from_id) + "") != False) :
        Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"به منوی اصلی ربات خوش امدید🎉\n\n💮 از دکمه های زیر استفاده کنید👇"),('reply_markup',json.dumps(OrderedDict([('keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"دریافت جایزه شما")]))])),(1,OrderedDict([(0,OrderedDict([('text',"🏅 زیر مجموعه های شما")]))])),(2,OrderedDict([(0,OrderedDict([('text',"📍 پشتیبانی")])),(1,OrderedDict([('text',"🔖 راهنما")])),(2,OrderedDict([('text',"🤖 درباره ربات")]))]))])),('resize_keyboard',True)])))]));
    else : 
        file_put_contents("data/" + str(from_id) + "/numchat.txt", "4");
        file_put_contents("data/" + str(from_id) + "/member.txt", "0");
        file_put_contents("data/" + str(from_id) + "/like.txt", "0");
        file_put_contents("data/" + str(from_id) + "/deslike.txt", "0");
        Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"سلام دوست گرامی به ربات جایزه بگیر تیم نازروید خوش اومدی میتونی با دعوت دوستات به این ربات از جوایز ویژه ما بهرهمند بشی\n  \n\n📣 جوایز ویژه هفتگی🙈\n\n📣 جوایز ویژه هفتگی🙈\n\n🌿 جوایز خاص فقط برای شما👇\n\n\n📅 " + str(date) + "\n🕗 " + str(time) + "\n🤖 " + str(usernamebot) + "")]));
        file_put_contents("data/" + str(from_id) + "/name.txt", "" + str(first_name) + "");
    

#**********
#***********
if (Source_Home == "🔙 برگشت" and tc == "private") :
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"به منوی اصلی ربات خوش امدید🎉\n\n💮 از دکمه های زیر استفاده کنید👇"),('reply_markup',json.dumps(OrderedDict([('keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"دریافت جایزه شما")]))])),(1,OrderedDict([(0,OrderedDict([('text',"🏅 زیر مجموعه های شما")]))])),(2,OrderedDict([(0,OrderedDict([('text',"📍 پشتیبانی")])),(1,OrderedDict([('text',"🔖 راهنما")])),(2,OrderedDict([('text',"🤖 درباره ربات")]))]))])),('resize_keyboard',True)])))]));
    file_put_contents("data/" + str(from_id) + "/chat.txt", "none");
    now = str_replace("" + str(from_id) + "\n", "", member);
    file_put_contents("data/chat.txt", "" + str(now) + "");
    file_put_contents("data/" + str(from_id) + "/file.txt", "none");
elif (Source_Home == "دریافت جایزه شما" and tc == "private") :
    if (vip != "") :
        memberex = member.split("\n");
        howmember = len(memberex) - 1;
        randmember = memberex[mt_rand(0, howmember)];
        if (randmember != "" and randmember != from_id) :
            file_put_contents("data/" + str(from_id) + "/chat.txt", "chatnashnas");
            file_put_contents("data/" + str(randmember) + "/chat.txt", "chatnashnas");
            file_put_contents("data/" + str(randmember) + "/nashnas.txt", "" + str(from_id) + "");
            file_put_contents("data/" + str(from_id) + "/nashnas.txt", "" + str(randmember) + "");
            aval = str_replace("" + str(from_id) + "\n", "", member);
            member = file_get_contents('data/chat.txt');
            file_put_contents("data/chat.txt", "" + str(aval) + "");
            dovom = str_replace("" + str(randmember) + "\n", "", member);
            file_put_contents("data/chat.txt", "" + str(dovom) + "");
            getuserprofile = getUserProfilePhotos(token, randmember);
            cuphoto = getuserprofile.total_count;
            getuserphoto = getuserprofile.photos[0][0].file_id;
            getuserprofile2 = getUserProfilePhotos(token, from_id);
            cuphoto2 = getuserprofile2.total_count;
            getuserphoto2 = getuserprofile2.photos[0][0].file_id;
            like = file_get_contents("data/" + str(randmember) + "/like.txt");
            deslike = file_get_contents("data/" + str(randmember) + "/deslike.txt");
            like2 = file_get_contents("data/" + str(from_id) + "/like.txt");
            deslike2 = file_get_contents("data/" + str(from_id) + "/deslike.txt");
            Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"📣 برای گرفتن جوایز آماده باش 🙈\n\n📅 " + str(date) + "\n🕗 " + str(time) + "\n🤖 " + str(usernamebot) + "")]));
        else : 
            Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"🤖 با تشکر از شما :\n\nاز لینک زیر میتونی برنامه آموزش زبان انگلیسی رو دانلود کنی👇👇\nhttps://nazroid.ir/1398/02/learning-english-with-paria-akhavass/")]));
        
    else : 
        Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"دوست عزیز توهم به راحتی میتونی از ما جایزه بگیری 😞\n\t\nکافیه همین الان روی دکمه دعوت دوستان کلیک کنی و  10 نفر از دوستات رو عضو ربات کنی🎯\n\nبعدشم جایزه ت رو بگیری😍"),('reply_markup',json.dumps(OrderedDict([('keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"⭐️ دعوت دوستان")]))])),(1,OrderedDict([(0,OrderedDict([('text',"🔙 برگشت")]))]))])),('resize_keyboard',True)])))]));
    
 elif (Source_Home == "/vip" or Source_Home == "🏅 زیر مجموعه های شما" or Source_Home == "⭐️ دعوت دوستان" and tc == "private") :
    #************ tedad add ozv 10tA
    cheghadr = 10 - adds;
    Source_Home('sendphoto', OrderedDict([('chat_id',chat_id),('photo',"https://bit.ly/2VPDhuO"),('caption',"📣  ربات تلگرام افزایش ممبر کانال بصورت هرمی و زیر مجموعه گیری😁💦\n\n▫️ربات تلگرم افزایش ممبر کانال بصورت هرمی و زیر مجموعه گیری،با سرعت تصاعدی برای کانال و ربات تون ممبر واقعی و فعال جذب میکنه و همه چیز به صورت خودکار توسط ربات صورت میگیره.🙈\n\n🔖 سورس کد کامل ربات تلگرم افزایش ممبر کانال بصورت هرمی🤦🏼‍♀👇\n\n🌐 https://t.me/" + str(usernamebot) + "?start=" + str(from_id) + "")]));
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"👆🏻 بنر بالا حاوی لینک دعوت شماست ان رو برای دوستان و گروه و کانال خود ارسال کنید و با جمع اوری زیر مجموعه ربات خودتون رو رایگان ویژه کنید 👆🏻")]));
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"📌 تعداد افرادی که دعوت کرده اید : " + str(adds) + "\n\t\n🔱 تعداد نفراتی که باید دعوت کنید تا ربات ویژه شود : " + str(cheghadr) + "")]));

if (Source_Home == "🤖 درباره ربات" and tc == "private") :
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"🤖 ربات جایزه بگیر نازروید \n➖➖➖\n📍تمامی حقوق کد نویسی و انتشار این ربات برای سایت نازروید محفوظ است \n\n\n💠 WWW.NAZROID.IR\n\n✅ رباتی هوشمند برای جذب ممبر به صورت هرمی\n\n🆔 @" + str(usernamebot) + "")]));

if (Source_Home == "🔖 راهنما" and tc == "private") :
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"🤖 ربات جایزه بگیر نازروید \n➖➖➖➖➖\nبه بخش راهنمای ربات خوش آمدید 🔆\n\n1️⃣ قوانین ربات ساده است \n\n⚠️ دوستات رو عضو کن بعدشم جایزه ت رو بگیر\n\n\n🆔 @" + str(usernamebot) + "")]));

if (Source_Home == "📍 پشتیبانی" and tc == "private") :
    file_put_contents("data/" + str(from_id) + "/file.txt", "nazar");
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"نظرات شما باعث دلگرمی ماست❤️\n➖➖➖➖➖\nانتفادات پیشنهادات و نظرات خود را برای ما ارسال کنید✔️\n➖➖➖\nپیام خود را وارد کنید"),('reply_markup',json.dumps(OrderedDict([('resize_keyboard',True),('keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"🔙 برگشت")]))]))]))])))]));
elif (step == "nazar" and tc == "private") :
    if (Source_Home != "🔙 برگشت") :
        unlink("data/" + str(from_id) + ".txt");
        Source_Home('ForwardMessage', OrderedDict([('chat_id',Dev[0]),('from_chat_id',chat_id),('message_id',message_id)]));
        Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"✔️نظر شما ارسال شد.\nبا تشکر از شما")]));
    
 elif (update.message and rt and from_id == Dev[0] and tc == "private") :
    if (update.message.text) :
        Source_Home('sendmessage', OrderedDict([("chat_id",chat_id),("text","پیام شما برای فرد ارسال شد ✔️")]));
        Source_Home('sendmessage', OrderedDict([("chat_id",reply),("text","👤پاسخ پشتیبان برای شما :\n\n`" + str(Source_Home) + "`"),('parse_mode','MarkDown')]));
    

#************** test
if (Source_Home == "ادمینم" or Source_Home == "/panel" or Source_Home == "مدیریت" or Source_Home == "/start panel") :
    if (in_array(from_id, Dev) != False) :
        if (tc == "private") :
            Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"🚦ادمین عزیز به پنل مدریت ربات خوش امدید"),('reply_to_message_id',message_id),('reply_markup',json.dumps(OrderedDict([('keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"💥 امار ربات ")])),(1,OrderedDict([('text',"🔆 ویژه کردن")]))])),(1,OrderedDict([(0,OrderedDict([('text',"🔅 ارسال به همه")])),(1,OrderedDict([('text',"📍 فروارد همگانی")]))])),(2,OrderedDict([(0,OrderedDict([('text',"📌 افراد انلاین")])),(1,OrderedDict([('text',"⛔️ مسدود کردن")]))])),(3,OrderedDict([(0,OrderedDict([('text',"🔙 برگشت")]))]))])),('resize_keyboard',True)])))]));
        
    
elif (Source_Home == "⛔️ مسدود کردن") :
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"لطفا یک پیام از کاربر را فوروارد کنید یا ایدی عددی فرد را وارد کنید🚀"),('reply_markup',json.dumps(OrderedDict([('keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"برگشت 🔙")]))]))])),('resize_keyboard',True)])))]));
    file_put_contents("data/" + str(from_id) + "/file.txt", "block");
 elif (step == 'block') :
    if (Source_Home != "برگشت 🔙") :
        if (forward_from == True) :
            Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"کابر با موفقیت از ربات مسدود شد ✔️\n\n🔹ایدی : " + str(forward_from_id) + "\n🔸یوزرنیم : @" + str(forward_from_username) + ""),('reply_to_message_id',message_id)]));
            adduser = file_get_contents("data/blocklist.txt");
            adduser += str(forward_from_id) + "\n";
            file_put_contents("data/blocklist.txt", adduser);
            file_put_contents("data/" + str(from_id) + "/file.txt", "none");
        else : 
            Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"کابر با موفقیت از ربات مسدود شد ✔️\n\n🔹ایدی : " + str(Source_Home) + ""),('reply_to_message_id',message_id)]));
            adduser = file_get_contents("data/blocklist.txt");
            adduser += str(Source_Home) + "\n";
            file_put_contents("data/blocklist.txt", adduser);
            file_put_contents("data/" + str(from_id) + "/file.txt", "none");
        
    
 elif (Source_Home == "📌 افراد انلاین") :
    member1 = file_get_contents("data/chat.txt");
    member2 = member1.split("\n");
    how = len(member2) - 1;
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"🤖 تعداد افراد در انتظار چت ناشناس : " + str(how) + ""),('hide_keyboard',True)]));
 elif (Source_Home == "💥 امار ربات") :
    mmemcount = len(members) - 1;
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"🤖 امار ربات شما : " + str(mmemcount) + ""),('hide_keyboard',True)]));
 elif (Source_Home == '🔅 ارسال به همه') :
    file_put_contents("data/" + str(from_id) + "/file.txt", "sendtoall");
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"لطفا متن خود را ارسال کنید 🚀"),('reply_to_message_id',message_id),('reply_markup',json.dumps(OrderedDict([('keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"برگشت 🔙")]))]))])),('resize_keyboard',True)])))]));
 elif (step == 'sendtoall') :
    file_put_contents("data/" + str(from_id) + "/file.txt", "none");
    if (Source_Home != "برگشت 🔙") :
        Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"پیام با موفقیت ارسال شد✔️"),('reply_to_message_id',message_id)]));
        mem = open("Member.txt", 'r');
        while (not feof(mem)) :
            memuser = fgets(mem);
            Source_Home('sendmessage', OrderedDict([('chat_id',memuser),('text',Source_Home)]));
        
    
 elif (Source_Home == '📍 فروارد همگانی') :
    file_put_contents("data/" + str(from_id) + "/file.txt", "fortoall");
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"لطفا متن خود را فوروارد کنید 🚀"),('reply_to_message_id',message_id),('reply_markup',json.dumps(OrderedDict([('keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"برگشت 🔙")]))]))])),('resize_keyboard',True)])))]));
 elif (step == 'fortoall') :
    file_put_contents("data/" + str(from_id) + "/file.txt", "none");
    if (Source_Home != "برگشت 🔙") :
        Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"پیام با موفقیت ارسال شد✔️"),('reply_to_message_id',message_id)]));
        mem = open("Member.txt", 'r');
        while (not feof(mem)) :
            memuser = fgets(mem);
            Forward(memuser, chat_id, message_id);
        
    

if (Source_Home == 'برگشت 🔙') :
    file_put_contents("data/" + str(from_id) + ".txt", "none");
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"🚦ادمین عزیز به پنل مدریت ربات خوش امدید"),('reply_to_message_id',message_id),('reply_markup',json.dumps(OrderedDict([('keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"💥 امار ربات ")])),(1,OrderedDict([('text',"🔆 ویژه کردن")]))])),(1,OrderedDict([(0,OrderedDict([('text',"🔅 ارسال به همه")])),(1,OrderedDict([('text',"📍 فروارد همگانی")]))])),(2,OrderedDict([(0,OrderedDict([('text',"📌 افراد انلاین")])),(1,OrderedDict([('text',"⛔️ مسدود کردن")]))])),(3,OrderedDict([(0,OrderedDict([('text',"🔙 برگشت")]))]))])),('resize_keyboard',True)])))]));
elif (Source_Home == '🔆 ویژه کردن') :
    file_put_contents("data/" + str(from_id) + "/file.txt", "setvip");
    Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"لطفا یک پیام از کاربر را فوروارد کنید یا ایدی عددی فرد را وارد کنید🚀"),('reply_to_message_id',message_id),('reply_markup',json.dumps(OrderedDict([('keyboard',OrderedDict([(0,OrderedDict([(0,OrderedDict([('text',"برگشت 🔙")]))]))])),('resize_keyboard',True)])))]));
 elif (step == 'setvip') :
    if (Source_Home != "برگشت 🔙") :
        if (forward_from == True) :
            Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"کابر با موفقیت ویژه شد ✔️\n\n🔹ایدی : " + str(forward_from_id) + "\n🔸یوزرنیم : @" + str(forward_from_username) + ""),('reply_to_message_id',message_id)]));
            file_put_contents("data/" + str(forward_from_id) + "/vip.txt", "true");
            file_put_contents("data/" + str(forward_from_id) + "/member.txt", "10");
            file_put_contents("data/" + str(from_id) + "/file.txt", "none");
        else : 
            if (Source_Home != "برگشت 🔙") :
                Source_Home('sendmessage', OrderedDict([('chat_id',chat_id),('text',"کابر با موفقیت ویژه شد ✔️\n\n🔹ایدی : " + str(Source_Home) + ""),('reply_to_message_id',message_id)]));
                file_put_contents("data/" + str(Source_Home) + "/vip.txt", "true");
                file_put_contents("data/" + str(Source_Home) + "/member.txt", "10");
                file_put_contents("data/" + str(from_id) + "/file.txt", "none");
            
        
    

unlink("error_log");
