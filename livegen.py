import re,sys,random,time,os
from datetime import date, datetime

now = datetime.now()
datetime = now.strftime("%B %d, %Y 1/ %H:%M:%S")
print("TODAY'S DATE => ", datetime)

print("==")

area = [
"845", "951", "408", "513", "832", "918", "570", "971", "409", "901", "970", "318", "218", "320", "661", "419", "815", "801", "931", "443", "251", "773", "301", "216", "507", "605", "414", "424", "212", "346", "440", "504", "909", "219", "229", "903", "208", "859", "618", "314", "484", "765", "712", "919", "432", "817", "941", "915", "620", "616", "720", "559", "928", "302", "657", "716", "330", "231", "567", "972", "323", "319", "702", "508", "707", "813", "907", "978", "267", "304", "417", "574", "609", "413", "575", "770", "580", "623", "334", "714", "573", "781", "831", "917", "985", "406", "606", "906", "989", "407", "214", "254", "818", "470", "276", "435", "405", "701", "724", "802", "660", "307", "828", "501", "602", "727", "979", "480", "662", "681", "262", "206", "402", "775", "203", "515", "740", "626", "804", "732", "312", "601", "509", "352", "614", "619", "989", "510", "719", "706", "646", "512", "213", "863", "253", "347", "202", "956", "603", "442", "310", "410", "561", "949", "209", "630", "864", "678", "774", "228", "608", "252", "563", "704", "785", "857", "913", "805", "612", "731", "904", "313", "281", "503", "317", "760", "517", "215", "860", "337", "806", "336", "937", "360", "562", "843", "412", "385", "856", "641", "518", "865", "225", "734", "234", "786", "763", "703", "423", "256", "502", "940", "469", "912", "309", "973", "757", "607", "914", "929", "425", "325", "847", "434", "772", "303", "908", "830", "404", "910", "505", "308", "718", "850", "207", "479", "270", "315", "520", "210", "540", "571", "808", "617", "541", "401", "615", "516", "810", "386", "803", "205", "478", "248", "610", "713", "305", "870", "862", "239", "636", "269", "650", "240", "715", "717", "858", "925", "814", "651", "224", "316", "201", "217", "708", "916", "415", "530", "682", "816", "936", "952", "321", "361", "812", "980", "954", "260", "920", "631", "586", "585"
]

area2 = ["845","408","513","764","832","953","742","695","218","736","243","661","888","791","597","827","251","773","476","268","216","743","605","824","346","257","273","829","437","903","685","859","995","618","568","765","343","362","817","676","637","932","876","628","565","596","616","928","604","948","388","431","275","935","702","508","821","267","690","529","223","241","433","634","609","413","575","328","781","831","930","849","723","406","456","606","906","666","782","589","767","470","435","802","884","259","459","471","501","727","721","677","958","753","967","622","300","515","777","740","389","247","600","833","509","668","383","510","449","706","841","646","512","202","956","728","747","692","949","882","864","957","228","921","783","905","324","654","460","532","945","826","731","726","281","688","877","664","697","999","592","337","937","489","566","843","412","749","968","283","865","786","234","763","527","703","762","256","966","353","416","973","500","250","961","852","946","236","526","871","830","371","590","955","789","987","465","261","462","210","927","444","993","571","401","516","386","333","478","338","242","549","519","474","636","650","925","354","715","497","651","224","670","418","793","451","415","796","795","816","584","812","980","954","260","602","335","929","543","396","461","918","901","776","320","672","552","801","550","879","924","297","588","483","507","693","453","424","926","504","909","219","797","430","746","699","834","467","286","934","941","329","981","274","620","577","559","332","657","794","231","237","378","447","923","567","761","564","323","356","944","896","304","838","574","875","282","985","917","334","492","521", "276","724","200","979","349","643","382","679","262","204","922","264","402","895","804","626","326","368","377","522","687","784","719","295","986","756","825","347","591","581","990","263","768","345","464","226","495","296","348","792","293","322","612","809","904","741","649","313","503","317","271","557","790","517","215","227","524","481","385","393","548","892","518","853","225","438","446","807","494","769","656","469","341","757","607","914","854","839","872","587","394","505","751","820","292","308","982","496","270","959","363","755","399","477","696","898","365","617","810","205","280","370","610","713","938","305","870","665","836","490","239","230","595","766","621","272","482","916","530","952","380","321","361","683","851","700","535","951","572","379","374","780","778","970","902","318","815","419","443","358","506","648","771","737","545","266","244","301","867","233","290","939","208","975","450","314","997","712","436","432","538","837","594","855","663","452","439","720","725","716","738","787","221","758","560","710","680","653","331","277","813","978","707","798","891","486","735","770","448","633","573","366","355","407","254","818","862","828","405","705","307","886","569","684","480","662","681","593","455","485","498","521","206","203","752","994","899","369","429","525","601","614","800","359","998","989","635","863","265","887","603","442","547","310","561","387","209","391","893","579","678","531","608","913","367","327","421","350","583","730","624","873","860","806","336","840","562","445","729","639","641","291","992","423","502","722","940","988","823","963","652","942","779","733","576","425","759","694","325","933","847","434","613","965","427","689","868","750","339","463","554","850","468","718","207","479","542","457","278","878","344","539","974","541","625","248","392","880","342","686","578","398","426","717","638","269","858","220","249","466","947","599","936","556","640","631","983","709","586","991","553","395","570","971","409","644","822","632","931","487","976","866","883","284","673","889","414","285","212","440","493","659","229","748","279","960","484","533","919","627","582","745","915","523","381","397","375","302","488","874","298","330","972","458","969","319","536","907","232","848","499","372","417","846","996","299","714","475","580","623","667","551","245","214","376","384","491","701","544","674","660","964","306","514","472","977","788","775","546","357","645","739","943","732","312","352","619","558","473","400","213","253","698","691","410","744","630","454","528","774","857","642","252","563","704","785","537","390","805","294","890","340","351","675","760","835","360","598","754","819","885","856","734","235","869","655","912","309","881","669","289","772","303","908","404","910","246","441","287","315","629","255","520","671","238","540","288","422","808","984","615","803","900","658","364","799","373","842","897","240","534","420","428","814","258","316","201","217","894","844","962","708","682","222","403","647","920","861","585"
]

#sv = input("Enter the file name to save verified numbers (DON'T INCLUDE FILE EXTENSION e.g .txt): ")
#print("==")
#cc = input(str('Enter the Country Code { EX +1 For USA } : '))
#print("==")
n = int(input("[+] Enter Amount of numbers to Generate: "))
print("==")
sv = input("[+] TXT file to save to: ")
print("==")
lent = 4
#lent = int(input('Length Remaining Digits [ 7 FOR USA ] : '))
#print('-'*33)
mow = str('9'*lent)

# Open the file in write mode and truncate it
with open("gen.txt", "w") as file:
    file.truncate()

print("Content of the file deleted.")

with open(sv, "w") as file:
    file.truncate()

print("Content of the file deleted.")


def gen():
    for i in range(0,n):
        first = (random.choice(area) + random.choice(area2) + str(random.randint(0,int(mow))).zfill(lent))
        with open('gen.txt', 'a') as save:
            save.write(first + "\n")
    print('Phone Numbers Saved In gen.txt')
gen()
        
def check_carrier(string):
    Verizon = ["Verizon", "Cellco"]
    Att = ["At&t", "New Cingular Wireless"]
    Tmobile = ["T-mobile", "Sprint Spectrum"]

    if any(keyword in string for keyword in Verizon):
        return "Verizon"
    elif any(keyword in string for keyword in Att):
        return "AT&T"
    elif any(keyword in string for keyword in Tmobile):
        return "T-Mobile"
    else:
        return "Unknown"
        
#num = open("gen.txt", mode='r', encoding='utf-8').read().split('\n')

with open("gen.txt", "r") as num1, open("carriers.txt", "r") as car1:
    num = num1.read().split('\n')
    car = car1.read().split('\n')
def verify():
        for line in num:
            for i in car:            
                line1 = line[0:6]
                i1 = i[3:6] + i[7:11]
                parts = i.split(':')
                if len(parts) >= 5:
                    content = parts[4]
                #if line1.strip() == i1.strip():
                if line1.strip() == i1.strip() and "Verizon" in i:
                    with open(sv, 'a') as save:
                        save.write("+1" + line + "\n")
                        print ("[+] Found " + line + ": " + content.strip())
                        result = check_carrier(content.strip())
                        if result:
                            print ("[+] " + line + " >> " + result)
                            print("==")
                            
verify()

def remove_duplicates(filename):
    # Read the file content
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove duplicate lines
    lines = list(set(lines))

    # Write the updated content back to the file
    with open(filename, 'w') as file:
        file.writelines(lines)

# Example usage
filename = sv
remove_duplicates(filename)
                        
print("Verified Numbers Saved In " + sv)
print("==")
