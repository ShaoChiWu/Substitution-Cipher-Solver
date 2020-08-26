import random
import ngram_score as ns

fitness = ns.ngram_score('english_quadgrams.txt')
essay_raw = "qqlcsutswydckoknlHfsytsuytsdckabtnItldzhffbiyhxqhmysqdclyhfonctiacnbybtiHtxlcsfkwytwyhqitfsytsfubbsfbnDckiclcsxbtlscihbuhsyyhxDckfubtnhsxdjkbblTfubtnhsfybfthihlsybWcxxclSclmkbcasybFbeblZhlmicxfsytsodnhmysfubnbybnfSybsyhniqbebqcasybrqtsacnxutfuceblcaontlwybflcsyhwzbnsytltahlmbntliwcebnbiuhsyindqbtebftlisuhmfSybdqthisybxlcnsyscfcksyancxhwbscahnbtlirhqbisybxyhmyuhsyfcaswkfyhclftlifqbbrhlmfhqzfSybfklytiobmklscqcubnscutnisybubfsodsybshxbsybdubnbiclbItldwtqqbisybIcsyntzhtnckliybnAbubnsytltyklinbiubnbqbasYcuxtldytiTbmclfstnsbiuhsyfybuclibnbiHsihilcsxtssbnDckuhqqobxdzytqtftnfybscqisybxHfbbsybatwbfcafqtebfHanbbdckStzbcaadcknwcqqtnfMchadckuhfylcclbfytqqytnxdckHadckfstdhsuhqqobtfoncsybnftlifhfsbnfykfotliftliuhebfSyboqtwzbdbfutswybiybnutndbgrnbffhclqbffHfbbsybwyhqinblucxblsybunhlzqbiatwbfcasybtmbiHutftwyhqidbfsbnitdScitdHtxtucxtlScxcnncuHuhqqobcqiScbtwycadckHftdmhebxbdcknytliftlidcknybtnsftlisybnbuhqqtqutdfobtrqtwbacndckFybsknlbiscsybsynbbdcklmutnnhcnfcaybnzytfVycmcscdckHmhebsybfhqebnytliqbiuyhrsytsutfxdonhibmhastliltxbdckzctlitfzdcknctsysytsdckuhqqqhebtliihbtfoqccicaxdoqccinhihlmtsxdfhibsczbbrxbftabancxytnxVycmcscczsybuyhrancxybnytlifoksyhfatwbutfwclakfbiZytqbbfhybfthiybfhstlsqdsyhfhflcsiclbHsuckqifytxbxbscoboqccinhibnsctucxtlRtmbTmmcItldwtqqbirtdhlmlcybbiscVycmcfucnifHaHqcczotwzHtxqcfsScdckHmhebsybintmcloclbocusytsutfxdonhibmhasHsutfickoqbwknebifyhldoqtwztlibgjkhfhsbstqqbnsytlfybutfHltxbdckzctlitfzdcknctsysytsdckfyckqiqhebtliihbtfoqccicaxdoqccinhihlmtsxdfhibsczbbrxbftabancxytnxTmmctwwbrsbisybocuuhsyqcubnbibdbfHwtllcsftdsybfbucnifClqdtxtlwtlqbtitzytqtftncnltxbtzcNtzytncItldfthisknlhlmtutdancxsybnbakftqdckfytqqytebsybmnbtstntzysytsutfxdonhibmhasuhsyyhqstlioqtibwytfbihlmcqiTlidcksccHltxbxdzctlitfzsytsdckqhebtliihbtfoqccicaxdoqccinhihlmtsxdfhibsczbbrxbftabancxytnxDcktnbzytqbbfhNtzytncfthistzhlmsybtntzyHfytqqnhibtsdcknfhibscEtbfIcsyntzoblbtsysybXcsybncaXcklsthlftlizbbrdckftabancxytnxklshqdckstzbdcknrqtwbuhsysybwnclbfcasybicfyzytqbblLcxcnbwtlHrncxhfbFyblciibitfwtqxqdtfhafybytilcsybtniyhftlfubntlisknlbiscsybqtfscaybnwytxrhclfFbnVcntyXcnxclsfybfthiahnfstlimnbtsbfscaxdzlhmysfHyteblconhibmhasscmhebdckoksHfubtnscdckclbitddckfytqqytebancxxdytliftqclmfucniqhzblclbsybucnqiytfbebnfbblintmclacnmbitlixtibcaEtqdnhtlfsbbqTliHuckqitfzacndcknctsytfubqqDckytebhsxdjkbblFbnVcntyfthizlbbqhlmscqtdyhffucnitsybnabbsHecuscfbnebdcksccobddckscihbacndckhalbbiobUytsbebnxtdwcxbUytsbebnxtdwcxbHfytqqycqidckscsytsctsyHrntddcklbebnnbmnbssybmhehlmcahsItldqhasbiyhxscyhfabbsRtmbFsnbswyhlmclybnscbfscnbtwyyhfqhrffybzhffbisybzlhmysmblsqdtlifthiDcktnbsybahnfscaxdJkbblfmktniFybwckqiabbqsybbdbfcasybzytqtftnclybntffybblsbnbiybnsblsSybIcsyntzhubnbxkssbnhlmtlimhehlmybnfsntlmbfhibutdfqcczfancxsybwcnlbnfcasybhnitnztqxclibdbfSybdsyckmysybnxtiItldnbtqhpbiRbnytrffybutfFybuckqizlcufcclblckmyHaHqcczotwzHtxqcfsYbnotsyutffwtqihlmycsuyblHnnhybqrbiybnhlscsybskooksItldihilcsaqhlwycnwndtqckiFybqhzbisybybtsHsxtibybnabbqwqbtlVyhjkhytifwblsbisybutsbnuhsysybchqffybytiacklihlsybxtnzbshlEtbfIcsyntzsybfsbtxncfbxchfstliantmntlsIcnbtyutfybiybnythntliwcxobihscksucnzhlmqccfbsybxtsftlistlmqbfHnnhfwnkoobiybnotwzItldwqcfbiybnbdbftliqbssybfxbqqtlisybutnxsyblacqiybnFybwckqiabbqsybybtsfctzhlmsynckmysybfcnblbffobsubblybnsyhmyfFybfykiibnbiuyblhsblsbnbiybntliybnrthltlifshaalbfffbbxbiscihffcqebFybaqctsbiUyblfybutfwqbtlybnytlixthifybqrbiybnancxsybutsbnHnnhtliVyhjkhatllbiybninduyhqbIcnbtyonkfybiybnythnklshqhsabqqqhzbtnhebncaqhjkhifhqebniculybnotwzSybdfwblsbiybnuhsyfrhwbaqcubntliwhlltxcltsckwyclbtwyunhfsobyhliybnbtnfclsybshrfcaybnxhqzybtedonbtfsfSybqtfsitoutfacnybnfbgHnnhfahlmbnabqstfqhmystliwccqtftqcebnfzhfftfhsfqhifcasqdkrobsubblybnqhrfTasbnutniItldfblssybxtqqtutdfcfybxhmysrnbrtnbZytqIncmcacnyhfahltqnhibhlscsyblhmysqtlifFybutfybiyhfocidwqbtltlionkfybitlichqbiyhfythnnkllhlmybnahlmbnfsynckmyhsacnsybqtfsshxbabbqhlmsybubhmyscahsnbxbxobnhlmsybahnfsshxbfybytisckwybihssyblhmyscasybhnubiihlmnhibYhfythnytilbebnobblwksYcuxtldxblwckqiihbuhsysybhnythnklwksFyboknhbiybnatwbhlhstlihlytqbisybitnzantmntlwbcasybchqfYbfxbqqbiqhzbmntfftliutnxbtnsyqhzbfxczbtlifbxbltliycnfbfYbfxbqqbiqhzbIncmcAcnmhebxbfklcaxdqhabfybsyckmysAcnmhebxbacntqqHytebiclbtlitqqHxkfsicHrthisybrnhwbxdfstnokshsutfsccyhmysccyhmyItldonthibiyhfythntlifqhisybfhqebnnhlmfclscyhfxkfstwybtliyklmyhfobqqfclbodclbFcxtldobqqfmcqitlifhqebntlionclpbObqqffcyhfblbxhbfuckqiybtnyhxwcxhlmtlimncuubtzuhsyabtnFybinbffbiyhxhlycnfbythnqbmmhlmftliyhmyoccsfokwzqhlmtobqsybteduhsymcqitlifhqebnxbitqqhclftocksyhfuthfsCebnyhffwtnnbiwybfsfybfqhrrbitrthlsbiebfscqitliatibisybclbIncmcytiqcebiobfsAcnybnfbqafybwycfbqccfbftlifhqzsnckfbnfftlitqfsytsqtwbiytqautdkrybnqbmftlitRtmbebfsqhzbIncmcfSybfklutfmchlmiculuyblfybwtqqbisybxotwzscwtnndyhfocidscsybrdnbSybIcsyntzhutswybihlfhqblwbtfVycmctliTmmcocnbyhxancxsybsblsItldutqzbiobyhlisybxSybdqthiyhxiculclyhfwkfyhclftlifhqzfyhfybtiscutnisybXcsybncaXcklsthlfatnscsyblcnsybtfsChqfybwcxxtlibitlisybdonckmysacnsysybvtnftlircknbisybxcebnsybrdnbfctzhlmsybfhqzftlisybonkfytlisybokliqbfcaindmntffklshqsybchqsnhwzqbiancxoblbtsysybqcmftlisybthnutfnhwyuhsyantmntlwbOnhlmxdbmmfItldwcxxtlibiybnytlixthifFcxbsyhlmhlybnechwbxtibsybxnklFbnVcntyscczybntnxXdjkbblIncmcuhqqyteblckfbacnintmclfbmmfhlsyblhmysqtlifObssbnscfbqqsybxhlTffythFbqqclbtliubwtlokdtfyhrscstzbkfotwzscsybAnbbWhshbfFbqqtqqsynbbtlidckuhqqobtubtqsyducxtltqqdcknitdfSybdubnblcsmheblscxbscfbqqItldscqiyhxFybwqhxobisybrdnbybnfbqascrqtwbsybbmmftnckliybnfkltlifstnfSyboqtwzobfhibyhfybtnsklibnyhftnxSybmnbblobfhibyhfybtiyhfonthiwchqbitncklihsSybwnbtxtlimcqiiculobsubblyhfqbmfUyblfybzhffbiyhxacnsybqtfsshxbItldwckqistfsbsybfubbslbffcasybchqclyhfqhrfTffybwqhxobiiculcaasybrdnbfyblcshwbiXhnnhXtpIkknutswyhlmybnDcktnbxtisybmcifuhabfthiyctnfbqdHfhsfcatnancxxtilbffscuhficxItldtfzbiFbnVcntystzbsyhfxtbmhtliohliybnscsybrdnbScsybxdjkbbllcybtnxbIctfHftdFshqqybybfhstsbiklshqybntlmbnaqtnbiDckfucnbsccobdxbuytsbebnxhmyswcxbNtzytncybqryhxRtmbSybmcifuhabihilcswndckstfsybdintmmbiybnscZytqIncmcfrdnbtlifstzbiybnicultxhifsyhfsnbtfknbfItldrcknbisybchqcebnsybucxtlfybtiybnfbqaHsytlzdckXhnnhXtpIkknfybfthiacnsybqbffclfdckytebstkmysxbDckuhqqlcsybtnxbfwnbtxXhnnhnbfrclibitfsybchqinhrrbiancxybnythntlifctzbiybnwqcsyhlmHuhqqItldfthiokshshflcsdcknfwnbtxfHutlsclqddcknqhabHnbxbxobnuytsdckscqixbClqdibtsywtlrtdacnqhabXhnnhXtpIkkncrblbiybnxcksyoksxtiblcnbrqdTffybfsbrrbitutdItldftusytssybwclsbxrsutfmclbancxsybxtbmhfaqtsoqtwzbdbfhlhsfrqtwbutffcxbsyhlmsytsxhmysytebobblabtnSyblsybnbutflcsyhlmscobiclboksutswysybfkltliqcczacnsybahnfsfstnUybltycnfbqcniihbfyhfycnfbhffqthluhsyyhxfcybxhmysnhibTMTXBCASYNCLQFrnckihlscsyblhmysqtlifSybocihbftnboknlbioblbtsysybcrblfzdtlisybzytqnhfbfclyhfahbndfsbbiscstzbyhfrqtwbtxclmsybfstnfSybxcnbahbnwbqdsybxtloknlbihlqhabsybonhmysbnyhffstnuhqqfyhlbhlsybitnzlbffVycmcfrhbihsahnfsSybnbybfthihltykfybiechwbItldqcczbitliftuhsqcuhlsybbtfsSybahnfsfstnutftwcxbsoknlhlmnbiOqccinbiahnbnbisybintmclfsthqFybwckqilcsytebtfzbiacntfsnclmbnfhmlItldscczsybscnwyancxTmmcfytlitlisynkfshsobsubblsybqcmfSybchqscczsybahnbtsclwbsybonkfytliinhbimntfftybtnsobtsqtsbnShldaqtxbfublsitnshlmkrsybucciqhzbfuhasnbixhwbfztshlmcebnsybchqtliqbtrhlmancxotnzscontlwyscqbtaTnhfhlmybtsrkaabitsybnatwbfcastlifkiibltftqcebnfonbtsyokshlfbwclifhsytimnculsccycsscobtnItldfsbrrbiotwzutniSybucciwntwzqbiqckibntliqckibnXhnnhXtpIkknobmtlscfhlmhltfynhqqkqkqtshlmechwbSybaqtxbfuyhnqbitliunhsybintwhlmbtwycsybnkrsybrqtsacnxSybikfzfyhxxbnbitfsybthnhsfbqafbbxbiscqhjkbadancxsybybtsItldybtniqcmffrhstliwntwzSybahnbffubrscebnXhnnhXtpIkknYbnfclmmnbuqckibnfynhqqbnsyblfybmtfrbitmthltlitmthltliybnfclmobwtxbtfykiibnhlmuthqsyhltliyhmytliakqqcatmcldRtmbTlilcusybaqtxbfnbtwybiybnIncmctlilcusybdubnbtqqtnckliyhxYhfwqcsyhlmscczahnbtliacntlhlfstlssybzytqutfwqtihluhfrfcaaqctshlmcntlmbfhqztlisblinhqfcawknqhlmfxczbmnbdtlimnbtfdItldfqhrfrtnsbitlifybackliybnfbqaycqihlmybnonbtsyRtnscaybnutlsbiscmcscyhxtfFbnVcntyytiabtnbiscnkfyhlscsybaqtxbfscobmacnyhfacnmheblbfftlistzbyhxhlfhibybnclbqtfsshxbsybahnbxbqshlmsybaqbfyancxsybhnoclbfklshqsybdubnbtfclbacnbebnFybwckqifxbqqsybcicncaoknlhlmaqbfylcihaabnblssytlycnfbaqbfynctfshlmhltahnbrhsSybrdnbnctnbihlsybibbrblhlmikfzqhzbfcxbmnbtsobtfsinculhlmckssybathlsbnfcklicaXhnnhXtpIkknffwnbtxhlmtlifblihlmkrqclmsclmkbfcaaqtxbscqhwztssybobqqdcasyblhmysTfsybfxczbmnbusyhwzbnsybIcsyntzhotwzbitutdwckmyhlmYkmbcntlmbmcksfcaahnbklaknqbisybhnotllbnfhlsytsybqqhfyuhlisybqcmfyhffhlmtliwntwzhlmmqcuhlmwhlibnfnhfhlmclsybfxczbscaqctstutdhlscsybitnzqhzbfcxtldlbuocnlahnbaqhbfSybybtsobtstssybthnuhsymnbtsnbiuhlmfinhehlmsybIcsyntzhotwzinhehlmcaabeblXcnxclsoksItldfscciybnmnckliFybutfsyboqccicasybintmcltlisybahnbutfhlybnFybytifblfbisybsnksycahsqclmtmcItldsyckmystffybsccztfsbrwqcfbnscsybwclaqtmntshclokssybontphbnytilcsobblycsblckmySybaqtxbfunhsybiobacnbybnqhzbsybucxbluycytiitlwbitsybnubiihlmuyhnqhlmtlifhlmhlmtlifrhllhlmsybhndbqqcutlicntlmbtliwnhxfclebhqfabtnfcxbscobycqidbsqcebqdfcqcebqdtqhebuhsyybtsItldcrblbiybntnxfscsybxybnfzhlaqkfybitlimqcuhlmSyhfhftubiihlmsccfybsyckmysXhnnhXtpIkknytiatqqblfhqblsSybmcifuhabsyckmysybntwyhqiokswyhqinblmncutliwyhqinblqbtnlTlcsybnfsbrtliItldwckqiabbqsybybtscasybftliclsybfcqbfcaybnabbsbeblsynckmyybnftlitqfFubtsntliculybnsyhmyftliobsubblybnonbtfsftlihlnhekqbsfcebnybnwybbzfuybnbsbtnfyticlwbnklFbnVcntyutffyckshlmobyhliybnoksybihilcsxtssbntldxcnbclqdsybahnbxtssbnbiSybaqtxbfubnbfcobtkshakqsybqcebqhbfssyhlmffybytibebnfbblbtwyclbtfcnwbnbnncobihldbqqcutlicntlmbtlifwtnqbsfuhnqhlmqclmfxczdwqctzfFybftuwnhxfclahnbqhclftlimnbtsdbqqcufbnrblsftliklhwcnlfxtibcartqboqkbaqtxbfybftuahfytliacgbftlixclfsbnfucqebftlionhmysohniftliaqcubnhlmsnbbfbtwyxcnbobtkshakqsytlsybqtfsFybftutycnfbtmnbtsmnbdfstqqhclqhxlbihlfxczbhsfaqcuhlmxtlbtlhxokfcaoqkbaqtxbDbfxdqcebxdfkltlifstnfdbfxcklslcushiblcuYbnebfsytiobmklscfxcqibnfcItldfynkmmbihscaatliqbshsatqqscsybmnckliSybrthlsbiqbtsybnoknfshlscfkiiblaqtxbtffybfzhrrbiwqcfbnscsybahnbybnonbtfsfotnbscsyboqtpbfsnbtxfcaxhqzaqcuhlmancxybnnbitlifucqqbllhrrqbfLcufybsyckmyslcutliacntlhlfstlsfybmqhxrfbiZytqIncmcobacnbybnxcklsbiclyhffxczdfstqqhcltaqtxhlmqtfyhlyhfytliYbfxhqbitlisybuyhrRtmbfltzbiicultssybrdnbyhffhlmFybybtnitwntwzsybfcklicafytssbnhlmfsclbSybrqtsacnxcauccitlionkfytlimntffobmtlscfyhastl"
essay = essay_raw.upper()

def replace(input1, input2, essay):
    output = ""
    for c in essay:
        for i in input1:
            if i == c:
                output=output+input2[input1.index(i)]
    #print(len(output))
    return output

def swap(key):
    new = ""
    a = 0
    b = 0
    while(a == b):
        a = random.randint(0,25)
        b = random.randint(0,25)
    for x in key:
        if key.index(x) == a:
            new += key[b]
        elif key.index(x) == b:
            new += key[a]
        else:
            new += x
    return new


def algo():
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    best_score = -7777777
    num_trails = 49
    num_swaps = 1999
    for i in range(1, num_trails, 1):
        key = ''.join(random.sample(s, len(s)))
        best_trail_score = -7777777
        for j in range(1, num_swaps, 1):
            new_key = swap(key)
            score = fitness.score(replace(s, new_key, essay))
            if score > best_trail_score:
                key = new_key
                best_trail_score = score
        if best_trail_score > best_score:
            best_key = key
            best_score = best_trail_score
        print(best_key, best_score)
    return best_key, best_score

def main():
    best_key, best_score = algo()
    flag = "OQHDALGFKAJESVYCJT"
    print(replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", best_key, flag))
    print(replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", best_key, essay))

main()