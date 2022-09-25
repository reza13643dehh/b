#!/usr/bin/env python
import datetime
import random
import threading
import time
from datetime import datetime
from bloomfilter import BloomFilter
from rich import print
import secp256k1 as ice

#  Mizogg.co.uk 2022  Bitty Looking for Bitcoin Addresses starting with 1 3 and bc1 Version 2

information = ('''
https://en.wikipedia.org/wiki/Bitcoin

Bitcoin (Abbreviation: BTC; sign: ₿) is a decentralized digital currency that can be transferred on the peer-to-peer bitcoin network.Bitcoin transactions are verified by network nodes through cryptography and recorded in a public distributed ledger called a blockchain. The cryptocurrency was invented in 2008 by an unknown person or group of people using the name Satoshi Nakamoto.The currency began use in 2009, when its implementation was released as open-source software.

Bitcoin has been described as an economic bubble by at least eight Nobel Memorial Prize in Economic Sciences recipients.

The word bitcoin was defined in a white paper published on 31 October 2008. It is a compound of the words bit and coin. No uniform convention for bitcoin capitalization exists; some sources use Bitcoin, capitalized, to refer to the technology and network and bitcoin, lowercase, for the unit of account.[15] The Wall Street Journal, The Chronicle of Higher Education, and the Oxford English Dictionary advocate the use of lowercase bitcoin in all cases.

The legality of bitcoin varies by region. Nine countries have fully banned bitcoin use, while a further fifteen have implicitly banned it. A few governments have used bitcoin in some capacity. El Salvador has adopted Bitcoin as legal tender, although use by merchants remains low. Ukraine has accepted cryptocurrency donations to fund the resistance to the 2022 Russian invasion. Iran has used bitcoin to bypass sanctions.

The unit of account of the bitcoin system is the bitcoin. Currency codes for representing bitcoin are BTC and XBT.
Its Unicode character is ₿. One bitcoin is divisible to eight decimal places. 
Units for smaller amounts of bitcoin are the millibitcoin (mBTC), equal to 1⁄1000 bitcoin, and the satoshi (sat), which is the smallest possible division, and named in homage to bitcoin's creator, representing 1⁄100000000 (one hundred millionth) bitcoin. 100,000 satoshis are one mBTC.
''')

#  Pages and WIFS Ranges
min_p = 1
max_p = 904625697166532776746648320380374280100293470930272690489102837043110636675
lines = '=' * 70

middle = 452312848583266388373324160190187140050146735465136345244551418521555318338
hj = 85966769946697919304477156997851416897897452779964215616135418886216209408
jk = 551340488851368173693535237984541213163631919119002481700768830238824024064
L1 = 398639737335773246472125555160783623763937797351505550641748492138749584881
L2 = 504075970525112600982146526634330530730393262381443907801548249398324792889
L3 = 609512203714451955492167498107877437696848727411382264961348006657900000897
L4 = 714948436903791310002188469581424344663304192441320622121147763917475208905
L5 = 820384670093130664512209441054971251629759657471258979280947521177050416913
Kx = 82331037767755182942062640740142902864571402261690479162349220360023960857
Ky = 187767270957094537452083612213689809831026867291628836322148977619599168865
Kz = 293203504146433891962104583687236716797482332321567193481948734879174376873

p1 = p2 = p3 = p4 = p5 = p6 = 1
p7 = 2
p8 = 3
p9 = 5
p10 = 9
p11 = 17
p12 = 33
p13 = 65
p14 = 129
p15 = 257
p16 = 513
p17 = 1025
p18 = 2049
p19 = 4097
p20 = 8193
p21 = 16385
p22 = 32769
p23 = 65537
p24 = 131073
p25 = 262145
p26 = 524289
p27 = 1048577
p28 = 2097153
p29 = 4194305
p30 = 8388609
p31 = 16777217
p32 = 33554433
p33 = 67108865
p34 = 134217729
p35 = 268435457
p36 = 536870913
p37 = 1073741825
p38 = 2147483649
p39 = 4294967297
p40 = 8589934593
p41 = 17179869185
p42 = 34359738369
p43 = 68719476737
p44 = 137438953473
p45 = 274877906945
p46 = 549755813889
p47 = 1099511627777
p48 = 2199023255553
p49 = 4398046511105
p50 = 8796093022209
p51 = 17592186044417
p52 = 35184372088833
p53 = 70368744177665
p54 = 140737488355329
p55 = 281474976710657
p56 = 562949953421313
p57 = 1125899906842625
p58 = 2251799813685249
p59 = 4503599627370497
p60 = 9007199254740993
p61 = 18014398509481985
p62 = 36028797018963969
p63 = 72057594037927937
p64 = 144115188075855873
p65 = 288230376151711745
p66 = 576460752303423489
p67 = 1152921504606846977
p68 = 2305843009213693953
p69 = 4611686018427387905
p70 = 9223372036854775809
p71 = 18446744073709551617
p72 = 36893488147419103233
p73 = 73786976294838206465
p74 = 147573952589676412929
p75 = 295147905179352825857
p76 = 590295810358705651713
p77 = 1180591620717411303425
p78 = 2361183241434822606849
p79 = 4722366482869645213697
p80 = 9444732965739290427393
p81 = 18889465931478580854785
p82 = 37778931862957161709569
p83 = 75557863725914323419137
p84 = 151115727451828646838273
p85 = 302231454903657293676545
p86 = 604462909807314587353089
p87 = 1208925819614629174706177
p88 = 2417851639229258349412353
p89 = 4835703278458516698824705
p90 = 9671406556917033397649409
p91 = 19342813113834066795298817
p92 = 38685626227668133590597633
p93 = 77371252455336267181195265
p94 = 154742504910672534362390529
p95 = 309485009821345068724781057
p96 = 618970019642690137449562113
p97 = 1237940039285380274899124225
p98 = 2475880078570760549798248449
p99 = 4951760157141521099596496897
p100 = 9903520314283042199192993793
p101 = 19807040628566084398385987585
p102 = 39614081257132168796771975169
p103 = 79228162514264337593543950337
p104 = 158456325028528675187087900673
p105 = 316912650057057350374175801345
p106 = 633825300114114700748351602689
p107 = 1267650600228229401496703205377
p108 = 2535301200456458802993406410753
p109 = 5070602400912917605986812821505
p110 = 10141204801825835211973625643009
p111 = 20282409603651670423947251286017
p112 = 40564819207303340847894502572033
p113 = 81129638414606681695789005144065
p114 = 162259276829213363391578010288129
p115 = 324518553658426726783156020576257
p116 = 649037107316853453566312041152513
p117 = 1298074214633706907132624082305025
p118 = 2596148429267413814265248164610049
p119 = 5192296858534827628530496329220097
p120 = 10384593717069655257060992658440193
p121 = 20769187434139310514121985316880385
p122 = 41538374868278621028243970633760769
p123 = 83076749736557242056487941267521537
p124 = 166153499473114484112975882535043073
p125 = 332306998946228968225951765070086145
p126 = 664613997892457936451903530140172289
p127 = 1329227995784915872903807060280344577
p128 = 2658455991569831745807614120560689153
p129 = 5316911983139663491615228241121378305
p130 = 10633823966279326983230456482242756609
p131 = 21267647932558653966460912964485513217
p132 = 42535295865117307932921825928971026433
p133 = 85070591730234615865843651857942052865
p134 = 170141183460469231731687303715884105729
p135 = 340282366920938463463374607431768211457
p136 = 680564733841876926926749214863536422913
p137 = 1361129467683753853853498429727072845825
p138 = 2722258935367507707706996859454145691649
p139 = 5444517870735015415413993718908291383297
p140 = 10889035741470030830827987437816582766593
p141 = 21778071482940061661655974875633165533185
p142 = 43556142965880123323311949751266331066369
p143 = 87112285931760246646623899502532662132737
p144 = 174224571863520493293247799005065324265473
p145 = 348449143727040986586495598010130648530945
p146 = 696898287454081973172991196020261297061889
p147 = 1393796574908163946345982392040522594123777
p148 = 2787593149816327892691964784081045188247553
p149 = 5575186299632655785383929568162090376495105
p150 = 11150372599265311570767859136324180752990209
p151 = 22300745198530623141535718272648361505980417
p152 = 44601490397061246283071436545296723011960833
p153 = 89202980794122492566142873090593446023921665
p154 = 178405961588244985132285746181186892047843329
p155 = 356811923176489970264571492362373784095686657
p156 = 713623846352979940529142984724747568191373313
p157 = 1427247692705959881058285969449495136382746625
p158 = 2854495385411919762116571938898990272765493249
p159 = 5708990770823839524233143877797980545530986497
p160 = 11417981541647679048466287755595961091061972993
p161 = 22835963083295358096932575511191922182123945985
p162 = 45671926166590716193865151022383844364247891969
p163 = 91343852333181432387730302044767688728495783937
p164 = 182687704666362864775460604089535377456991567873
p165 = 365375409332725729550921208179070754913983135745
p166 = 730750818665451459101842416358141509827966271489
p167 = 1461501637330902918203684832716283019655932542977
p168 = 2923003274661805836407369665432566039311865085953
p169 = 5846006549323611672814739330865132078623730171905
p170 = 11692013098647223345629478661730264157247460343809
p171 = 23384026197294446691258957323460528314494920687617
p172 = 46768052394588893382517914646921056628989841375233
p173 = 93536104789177786765035829293842113257979682750465
p174 = 187072209578355573530071658587684226515959365500929
p175 = 374144419156711147060143317175368453031918731001857
p176 = 748288838313422294120286634350736906063837462003713
p177 = 1496577676626844588240573268701473812127674924007425
p178 = 2993155353253689176481146537402947624255349848014849
p179 = 5986310706507378352962293074805895248510699696029697
p180 = 11972621413014756705924586149611790497021399392059393
p181 = 23945242826029513411849172299223580994042798784118785
p182 = 47890485652059026823698344598447161988085597568237569
p183 = 95780971304118053647396689196894323976171195136475137
p184 = 191561942608236107294793378393788647952342390272950273
p185 = 383123885216472214589586756787577295904684780545900545
p186 = 766247770432944429179173513575154591809369561091801089
p187 = 1532495540865888858358347027150309183618739122183602177
p188 = 3064991081731777716716694054300618367237478244367204353
p189 = 6129982163463555433433388108601236734474956488734408705
p190 = 12259964326927110866866776217202473468949912977468817409
p191 = 24519928653854221733733552434404946937899825954937634817
p192 = 49039857307708443467467104868809893875799651909875269633
p193 = 98079714615416886934934209737619787751599303819750539265
p194 = 196159429230833773869868419475239575503198607639501078529
p195 = 392318858461667547739736838950479151006397215279002157057
p196 = 784637716923335095479473677900958302012794430558004314113
p197 = 1569275433846670190958947355801916604025588861116008628225
p198 = 3138550867693340381917894711603833208051177722232017256449
p199 = 6277101735386680763835789423207666416102355444464034512897
p200 = 12554203470773361527671578846415332832204710888928069025793
p201 = 25108406941546723055343157692830665664409421777856138051585
p202 = 50216813883093446110686315385661331328818843555712276103169
p203 = 100433627766186892221372630771322662657637687111424552206337
p204 = 200867255532373784442745261542645325315275374222849104412673
p205 = 401734511064747568885490523085290650630550748445698208825345
p206 = 803469022129495137770981046170581301261101496891396417650689
p207 = 1606938044258990275541962092341162602522202993782792835301377
p208 = 3213876088517980551083924184682325205044405987565585670602753
p209 = 6427752177035961102167848369364650410088811975131171341205505
p210 = 12855504354071922204335696738729300820177623950262342682411009
p211 = 25711008708143844408671393477458601640355247900524685364822017
p212 = 51422017416287688817342786954917203280710495801049370729644033
p213 = 102844034832575377634685573909834406561420991602098741459288065
p214 = 205688069665150755269371147819668813122841983204197482918576129
p215 = 411376139330301510538742295639337626245683966408394965837152257
p216 = 822752278660603021077484591278675252491367932816789931674304513
p217 = 1645504557321206042154969182557350504982735865633579863348609025
p218 = 3291009114642412084309938365114701009965471731267159726697218049
p219 = 6582018229284824168619876730229402019930943462534319453394436097
p220 = 13164036458569648337239753460458804039861886925068638906788872193
p221 = 26328072917139296674479506920917608079723773850137277813577744385
p222 = 52656145834278593348959013841835216159447547700274555627155488769
p223 = 105312291668557186697918027683670432318895095400549111254310977537
p224 = 210624583337114373395836055367340864637790190801098222508621955073
p225 = 421249166674228746791672110734681729275580381602196445017243910145
p226 = 842498333348457493583344221469363458551160763204392890034487820289
p227 = 1684996666696914987166688442938726917102321526408785780068975640577
p228 = 3369993333393829974333376885877453834204643052817571560137951281153
p229 = 6739986666787659948666753771754907668409286105635143120275902562305
p230 = 13479973333575319897333507543509815336818572211270286240551805124609
p231 = 26959946667150639794667015087019630673637144422540572481103610249217
p232 = 53919893334301279589334030174039261347274288845081144962207220498433
p233 = 107839786668602559178668060348078522694548577690162289924414440996865
p234 = 215679573337205118357336120696157045389097155380324579848828881993729
p235 = 431359146674410236714672241392314090778194310760649159697657763987457
p236 = 862718293348820473429344482784628181556388621521298319395315527974913
p237 = 1725436586697640946858688965569256363112777243042596638790631055949825
p238 = 3450873173395281893717377931138512726225554486085193277581262111899649
p239 = 6901746346790563787434755862277025452451108972170386555162524223799297
p240 = 13803492693581127574869511724554050904902217944340773110325048447598593
p241 = 27606985387162255149739023449108101809804435888681546220650096895197185
p242 = 55213970774324510299478046898216203619608871777363092441300193790394369
p243 = 110427941548649020598956093796432407239217743554726184882600387580788737
p244 = 220855883097298041197912187592864814478435487109452369765200775161577473
p245 = 441711766194596082395824375185729628956870974218904739530401550323154945
p246 = 883423532389192164791648750371459257913741948437809479060803100646309889
p247 = 1766847064778384329583297500742918515827483896875618958121606201292619777
p248 = 3533694129556768659166595001485837031654967793751237916243212402585239553
p249 = 7067388259113537318333190002971674063309935587502475832486424805170479105
p250 = 14134776518227074636666380005943348126619871175004951664972849610340958209
p251 = 28269553036454149273332760011886696253239742350009903329945699220681916417
p252 = 56539106072908298546665520023773392506479484700019806659891398441363832833
p253 = 113078212145816597093331040047546785012958969400039613319782796882727665665
p254 = 226156424291633194186662080095093570025917938800079226639565593765455331329
p255 = 452312848583266388373324160190187140051835877600158453279131187530910662657

bitlist = (f'''
 Bits > 2^256 Max Page - {max_p}
 Bits > 2^255 Page - {p255}
 Bits > 2^254 Page - {p254}
 Bits > 2^253 Page - {p253}
 Bits > 2^252 Page - {p252}
 Bits > 2^251 Page - {p251}
 Bits > 2^250 Page - {p250}
			  
 Bits > 2^249 Page - {p249}
 Bits > 2^248 Page - {p248}
 Bits > 2^247 Page - {p247}
 Bits > 2^246 Page - {p246}
 Bits > 2^245 Page - {p245}
 Bits > 2^244 Page - {p244}
			  
 Bits > 2^243 Page - {p243}
 Bits > 2^242 Page - {p242}
 Bits > 2^241 Page - {p241}
 Bits > 2^240 Page - {p240}
 Bits > 2^239 Page - {p239}
 Bits > 2^238 Page - {p238}
			  
 Bits > 2^237 Page - {p237}
 Bits > 2^236 Page - {p236}
 Bits > 2^235 Page - {p235}
 Bits > 2^234 Page - {p234}
 Bits > 2^233 Page - {p233}
 Bits > 2^232 Page - {p232}
			  
 Bits > 2^231 Page - {p231}
 Bits > 2^230 Page - {p230}
 Bits > 2^229 Page - {p229}
 Bits > 2^228 Page - {p228}
 Bits > 2^227 Page - {p227}
 Bits > 2^226 Page - {p226}
			  
 Bits > 2^225 Page - {p225}
 Bits > 2^224 Page - {p224}
 Bits > 2^223 Page - {p223}
 Bits > 2^222 Page - {p222}
 Bits > 2^221 Page - {p221}
 Bits > 2^220 Page - {p220}
			  
 Bits > 2^219 Page - {p219}
 Bits > 2^218 Page - {p218}
 Bits > 2^217 Page - {p217}
 Bits > 2^216 Page - {p216}
 Bits > 2^215 Page - {p215}
 Bits > 2^214 Page - {p214}
			  
 Bits > 2^213 Page - {p213}
 Bits > 2^212 Page - {p212}
 Bits > 2^211 Page - {p211}
 Bits > 2^210 Page - {p210}
 Bits > 2^209 Page - {p209}
 Bits > 2^208 Page - {p208}
			  
 Bits > 2^207 Page - {p207}
 Bits > 2^206 Page - {p206}
 Bits > 2^205 Page - {p205}
 Bits > 2^204 Page - {p204}
 Bits > 2^203 Page - {p203}
 Bits > 2^202 Page - {p202}
			  
 Bits > 2^201 Page - {p201}
 Bits > 2^200 Page - {p200}
 Bits > 2^199 Page - {p199}
 Bits > 2^198 Page - {p198}
 Bits > 2^197 Page - {p197}
 Bits > 2^196 Page - {p196}
			  
 Bits > 2^195 Page - {p195}
 Bits > 2^194 Page - {p194}
 Bits > 2^193 Page - {p193}
 Bits > 2^192 Page - {p192}
 Bits > 2^191 Page - {p191}
 Bits > 2^190 Page - {p190}
			  
 Bits > 2^189 Page - {p189}
 Bits > 2^188 Page - {p188}
 Bits > 2^187 Page - {p187}
 Bits > 2^186 Page - {p186}
 Bits > 2^185 Page - {p185}
 Bits > 2^184 Page - {p184}
			  
 Bits > 2^183 Page - {p183}
 Bits > 2^182 Page - {p182}
 Bits > 2^181 Page - {p181}
 Bits > 2^180 Page - {p180}
 Bits > 2^179 Page - {p179}
 Bits > 2^178 Page - {p178}
			  
 Bits > 2^177 Page - {p177}
 Bits > 2^176 Page - {p176}
 Bits > 2^175 Page - {p175}
 Bits > 2^174 Page - {p174}
 Bits > 2^173 Page - {p173}
 Bits > 2^172 Page - {p172}
			  
 Bits > 2^171 Page - {p171}
 Bits > 2^170 Page - {p170}
 Bits > 2^169 Page - {p169}
 Bits > 2^168 Page - {p168}
 Bits > 2^167 Page - {p167}
 Bits > 2^166 Page - {p166}
			  
 Bits > 2^165 Page - {p165}
 Bits > 2^164 Page - {p164}
 Bits > 2^163 Page - {p163}
 Bits > 2^162 Page - {p162}
 Bits > 2^161 Page - {p161}
 Bits > 2^160 Page - {p160}
			  
 Bits > 2^159 Page - {p159}
 Bits > 2^158 Page - {p158}
 Bits > 2^157 Page - {p157}
 Bits > 2^156 Page - {p156}
 Bits > 2^155 Page - {p155}
 Bits > 2^154 Page - {p154}
			  
 Bits > 2^153 Page - {p153}
 Bits > 2^152 Page - {p152}
 Bits > 2^151 Page - {p151}
 Bits > 2^150 Page - {p150}
 Bits > 2^149 Page - {p149}
 Bits > 2^148 Page - {p148}
			  
 Bits > 2^147 Page - {p147}
 Bits > 2^146 Page - {p146}
 Bits > 2^145 Page - {p145}
 Bits > 2^144 Page - {p144}
 Bits > 2^143 Page - {p143}
 Bits > 2^142 Page - {p142}
			  
 Bits > 2^141 Page - {p141}
 Bits > 2^140 Page - {p140}
 Bits > 2^139 Page - {p139}
 Bits > 2^138 Page - {p138}
 Bits > 2^137 Page - {p137}
 Bits > 2^136 Page - {p136}
			  
 Bits > 2^135 Page - {p135}
 Bits > 2^134 Page - {p134}
 Bits > 2^133 Page - {p133}
 Bits > 2^132 Page - {p132}
 Bits > 2^131 Page - {p131}
 Bits > 2^130 Page - {p130}
			  
 Bits > 2^129 Page - {p129}
 Bits > 2^128 Page - {p128}
 Bits > 2^127 Page - {p127}
 Bits > 2^126 Page - {p126}
 Bits > 2^125 Page - {p125}
 Bits > 2^124 Page - {p124}
			  
 Bits > 2^123 Page - {p123}
 Bits > 2^122 Page - {p122}
 Bits > 2^121 Page - {p121}
 Bits > 2^120 Page - {p120}
 Bits > 2^119 Page - {p119}
 Bits > 2^118 Page - {p118}
			  
 Bits > 2^117 Page - {p117}
 Bits > 2^116 Page - {p116}
 Bits > 2^115 Page - {p115}
 Bits > 2^114 Page - {p114}
 Bits > 2^113 Page - {p113}
 Bits > 2^112 Page - {p112}
			  
 Bits > 2^111 Page - {p111}
 Bits > 2^110 Page - {p110}
 Bits > 2^109 Page - {p109}
 Bits > 2^108 Page - {p108}
 Bits > 2^107 Page - {p107}
 Bits > 2^106 Page - {p106}
			  
 Bits > 2^105 Page - {p105}
 Bits > 2^104 Page - {p104}
 Bits > 2^103 Page - {p103}
 Bits > 2^102 Page - {p102}
 Bits > 2^101 Page - {p101}
 Bits > 2^100 Page - {p100}

 Bits > 2^99 Page - {p99}
 Bits > 2^98 Page - {p98}
 Bits > 2^97 Page - {p97}
 Bits > 2^96 Page - {p96}
 Bits > 2^95 Page - {p95}
 Bits > 2^94 Page - {p94}
			 
 Bits > 2^93 Page - {p93}
 Bits > 2^92 Page - {p92}
 Bits > 2^91 Page - {p91}
 Bits > 2^90 Page - {p90}
 Bits > 2^89 Page - {p89}
 Bits > 2^88 Page - {p88}
			 
 Bits > 2^87 Page - {p87}
 Bits > 2^86 Page - {p86}
 Bits > 2^85 Page - {p85}
 Bits > 2^84 Page - {p84}
 Bits > 2^83 Page - {p83}
 Bits > 2^82 Page - {p82}
			 
 Bits > 2^81 Page - {p81}
 Bits > 2^82 Page - {p82}
 Bits > 2^81 Page - {p81}
 Bits > 2^80 Page - {p80}
 Bits > 2^79 Page - {p79}
 Bits > 2^78 Page - {p78}
			 
 Bits > 2^77 Page - {p77}
 Bits > 2^76 Page - {p76}
 Bits > 2^75 Page - {p75}
 Bits > 2^74 Page - {p74}
 Bits > 2^73 Page - {p73}
 Bits > 2^72 Page - {p72}
			 
 Bits > 2^71 Page - {p71}
 Bits > 2^70 Page - {p70}
 Bits > 2^69 Page - {p69}
 Bits > 2^68 Page - {p68}
 Bits > 2^67 Page - {p67}
 Bits > 2^66 Page - {p66}
			 
 Bits > 2^65 Page - {p65}
 Bits > 2^64 Page - {p64}
 Bits > 2^63 Page - {p63}
 Bits > 2^62 Page - {p62}
 Bits > 2^61 Page - {p61}
 Bits > 2^60 Page - {p60}
			 
 Bits > 2^59 Page - {p59}
 Bits > 2^58 Page - {p58}
 Bits > 2^57 Page - {p57}
 Bits > 2^56 Page - {p56}
 Bits > 2^55 Page - {p55}
 Bits > 2^54 Page - {p54}
			 
 Bits > 2^53 Page - {p53}
 Bits > 2^52 Page - {p52}
 Bits > 2^51 Page - {p51}
 Bits > 2^50 Page - {p50}
 Bits > 2^49 Page - {p49}
 Bits > 2^48 Page - {p48}
			 
 Bits > 2^47 Page - {p47}
 Bits > 2^46 Page - {p46}
 Bits > 2^45 Page - {p45}
 Bits > 2^44 Page - {p44}
 Bits > 2^43 Page - {p43}
 Bits > 2^42 Page - {p42}
			 
 Bits > 2^41 Page - {p41}
 Bits > 2^40 Page - {p40}
 Bits > 2^39 Page - {p39}
 Bits > 2^38 Page - {p38}
 Bits > 2^37 Page - {p37}
 Bits > 2^36 Page - {p36}
			 
 Bits > 2^35 Page - {p35}
 Bits > 2^34 Page - {p34}
 Bits > 2^33 Page - {p33}
 Bits > 2^32 Page - {p32}
 Bits > 2^31 Page - {p31}
 Bits > 2^30 Page - {p30}
			 
 Bits > 2^29 Page - {p29}
 Bits > 2^28 Page - {p28}
 Bits > 2^27 Page - {p27}
 Bits > 2^26 Page - {p26}
 Bits > 2^25 Page - {p25}
 Bits > 2^24 Page - {p24}
			 
 Bits > 2^23 Page - {p23}
 Bits > 2^22 Page - {p22}
 Bits > 2^21 Page - {p21}
 Bits > 2^20 Page - {p20}
 Bits > 2^19 Page - {p19}
 Bits > 2^18 Page - {p18}
			 
 Bits > 2^17 Page - {p17}
 Bits > 2^16 Page - {p16}
 Bits > 2^15 Page - {p15}
 Bits > 2^14 Page - {p14}
 Bits > 2^13 Page - {p13}
 Bits > 2^12 Page - {p12}
			 
 Bits > 2^11 Page - {p11}
 Bits > 2^10 Page - {p10}
 Bits > 2^9 Page - {p9}
 Bits > 2^8 Page - {p8}
 Bits > 2^7 Page - {p7}
 Bits > 2^6 Page - {p6}
		    
 Bits > 2^5 Page - {p5}
 Bits > 2^4 Page - {p4}
 Bits > 2^3 Page - {p3}
 Bits > 2^2 Page - {p2}
 Bits > 2^1 Page - {p1}
 ''')
 
 
def RandomInteger(minN, maxN):
    return random.randrange(minN, maxN)


def load_settings():
    global start_range, end_range, stop, bloom_filterbtc
    load_addresses('puzzle.bf')
    addr_count = len(bloom_filterbtc)
    print('  Mizogg.co.uk 2022  Bitty Looking for Addresses starting with 1 3 and bc1 Version 2 ' )
    print('  This Program Requires BloomFilter File of Addresses and Icelands ice_secp256k1.dll  ' )
    print(f'  [{timing}]  Total Bitcoin addresses Loaded and Checking  : ' + str(addr_count))
    print(f' {lines}\n  A private key is basically just a number between 1Bit and 256Bits. \n  This Program generates keys for all of those numbers, \n  spread out over pages of 128 keys each page 512 Addresses Per Page. \n  To get Started Pick a Option Highlighed in Red \n {lines}')
    print(f'''
[red]  1.[/red] Search By Page Ranges
[red]  2.[/red] Search By DEC Ranges
[red]  3.[/red] Search By BIT Ranges
[red]  4.[/red] Search By HEX Ranges
[red]  5.[/red] Search By WIF Ranges
[red]  6.[/red] Information & ( Start MIN to MAX )
''')
    startingscan = int(input(' Pick a Option Highlighed in Red ->  -> '))
    
    if startingscan == 1:
        print('[yellow]  Start search... Pick Page to start \n( Min= 1 Max= 904625697166532776746648320380374280100293470930272690489102837043110636674 )  [/yellow] ')
        start_range = int(input(' starting  Page ->  -> '))
        print(f'[yellow]  Stop search... Pick Page to Stop \n( Min= 2 Max= {max_p} )  [/yellow] ')
        end_range = int(input('  Stop Page -> -> '))
    
    if startingscan == 2:
        print('[yellow]  Start search... Pick DEC to start \n( Min= 1 Max= 115792089237316195423570985008687907852837564279074904382605163141518161494335 )  [/yellow] ')
        startdec = (input(' starting  DEC ->  -> '))
        num = int(startdec, 10)
        num = num // 128
        start_range = num + 1
        print(f'[yellow]  Stop search... Pick DEC to Stop \n( Min= 256 Max= 115792089237316195423570985008687907852837564279074904382605163141518161494336 )  [/yellow] ')
        enddec = (input('  Stop DEC -> -> '))
        num1 = int(enddec, 10)
        num1 = num1 // 128
        end_range = num1 + 1
        
    if startingscan == 3:
        print(f'''
[red]  1.[/red]  1 Bit - 30 Bits   1 - 3fffffff  
[red]  2.[/red]  30 - 40 Bits 40000000 - ffffffffff 
[red]  3.[/red]  40 - 50 Bits 10000000000 - 3ffffffffffff 
[red]  4.[/red]  50 - 60 Bits 4000000000000 - fffffffffffffff
[red]  5.[/red]  60 - 65 Bits 1000000000000000 - 1ffffffffffffffff
[red]  6.[/red]  65 - 66 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  7.[/red]  66 - 67 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  8.[/red]  67 - 68 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  9.[/red]  68 - 69 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  10.[/red] 69 - 70 Bits 200000000000000000 - 3fffffffffffffffff
[red]  11.[/red] 70 - 71 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  12.[/red] 71 - 72 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  13.[/red] 72 - 73 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  14.[/red] 73 - 74 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  15.[/red] 74 - 75 Bits 4000000000000000000 - 7ffffffffffffffffff
[red]  16.[/red] 75 - 76 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  17.[/red] 76 - 77 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  18.[/red] 77 - 78 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  19.[/red] 78 - 79 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  20.[/red] 79 - 80 Bits 80000000000000000000 - ffffffffffffffffffff
[red]  21.[/red] 80 - 81 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  22.[/red] 81 - 82 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  23.[/red] 82 - 83 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  24.[/red] 83 - 84 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  25.[/red] 84 - 85 Bits 1000000000000000000000 - 1fffffffffffffffffffff
[red]  26.[/red] 85 - 86 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  27.[/red] 86 - 87 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  28.[/red] 87 - 88 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  29.[/red] 88 - 89 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  30.[/red] 89 - 90 Bits 20000000000000000000000 - 3ffffffffffffffffffffff
[red]  31.[/red] 90 - 91 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  32.[/red] 91 - 92 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  33.[/red] 92 - 93 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  34.[/red] 93 - 94 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  35.[/red] 94 - 95 Bits 400000000000000000000000 - 7fffffffffffffffffffffff
[red]  36.[/red] 95 - 96 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  37.[/red] 96 - 97 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  38.[/red] 97 - 98 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  39.[/red] 98 - 99 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  40.[/red] 99 - 100 Bits 8000000000000000000000000- fffffffffffffffffffffffff
[red]  41.[/red] 100 - 101 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  42.[/red] 101 - 102 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  43.[/red] 102 - 103 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  44.[/red] 103 - 104 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  45.[/red] 104 - 105 Bits 100000000000000000000000000 - 1ffffffffffffffffffffffffff
[red]  46.[/red] 105 - 106 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  47.[/red] 106 - 107 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  48.[/red] 107 - 108 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  49.[/red] 108 - 109 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  50.[/red] 109 - 110 Bits 2000000000000000000000000000 - 3fffffffffffffffffffffffffff
[red]  51.[/red] 110 - 111 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  52.[/red] 111 - 112 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  53.[/red] 112 - 113 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  54.[/red] 113 - 114 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  55.[/red] 114 - 115 Bits 40000000000000000000000000000 - 7ffffffffffffffffffffffffffff
[red]  56.[/red] 115 - 116 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  57.[/red] 116 - 117 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  58.[/red] 117 - 118 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  59.[/red] 118 - 119 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  60.[/red] 119 - 120 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  61.[/red] 120 - 121 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  62.[/red] 121 - 122 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  63.[/red] 122 - 123 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  64.[/red] 123 - 124 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  65.[/red] 124 - 125 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  66.[/red] 125 - 126 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  67.[/red] 126 - 127 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  68.[/red] 127 - 128 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  69.[/red] 128 - 129 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  70.[/red] 129 - 130 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  71.[/red] 130 - 131 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  72.[/red] 131 - 132 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  73.[/red] 132 - 133 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  74.[/red] 133 - 134 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  75.[/red] 134 - 135 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  76.[/red] 135 - 136 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  77.[/red] 136 - 137 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  78.[/red] 137 - 138 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  79.[/red] 138 - 139 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  80.[/red] 139 - 140 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  81.[/red] 140 - 141 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  82.[/red] 141 - 142 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  83.[/red] 142 - 143 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  84.[/red] 143 - 144 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  85.[/red] 144 - 145 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  86.[/red] 145 - 146 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  87.[/red] 146 - 147 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  88.[/red] 147 - 148 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  89.[/red] 148 - 149 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  90.[/red] 149 - 150 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  91.[/red] 150 - 151 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  92.[/red] 151 - 152 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  93.[/red] 152 - 153 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  94.[/red] 153 - 154 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  95.[/red] 154 - 155 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  96.[/red] 155 - 156 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  97.[/red] 156 - 157 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  98.[/red] 157 - 158 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  99.[/red] 158 - 159 Bits [red]Unsolved Puzzle in This Range[/red]
[red]  100.[/red]159 - 160 Bits [red]Unsolved Puzzle in This Range[/red]
''')
        startingBITS = int(input(' Pick BITS Range Option Highlighed in Red ->  -> '))
        if startingBITS == 1:
            start_range = p1
            end_range = p30
        if startingBITS == 2:
            start_range = p30
            end_range = p40
        if startingBITS == 3:
            start_range = p40
            end_range = p50
        if startingBITS == 4:
            start_range = p50
            end_range = p60
        if startingBITS == 5:
            start_range = p60
            end_range = p65
        if startingBITS == 6:
            start_range = p65
            end_range = p66
        if startingBITS == 7:
            start_range = p66
            end_range = p67
        if startingBITS == 8:
            start_range = p67
            end_range = p68
        if startingBITS == 9:
            start_range = p68
            end_range = p69
        if startingBITS == 10:
            start_range = p69
            end_range = p70
        if startingBITS == 11:
            start_range = p70
            end_range = p71
        if startingBITS == 12:
            start_range = p71
            end_range = p72
        if startingBITS == 13:
            start_range = p72
            end_range = p73
        if startingBITS == 14:
            start_range = p73
            end_range = p74
        if startingBITS == 15:
            start_range = p74
            end_range = p75
        if startingBITS == 16:
            start_range = p75
            end_range = p76
        if startingBITS == 17:
            start_range = p76
            end_range = p77
        if startingBITS == 18:
            start_range = p77
            end_range = p78
        if startingBITS == 19:
            start_range = p78
            end_range = p79
        if startingBITS == 20:
            start_range = p79
            end_range = p80
        if startingBITS == 21:
            start_range = p80
            end_range = p81
        if startingBITS == 22:
            start_range = p81
            end_range = p82
        if startingBITS == 23:
            start_range = p82
            end_range = p83
        if startingBITS == 24:
            start_range = p83
            end_range = p84
        if startingBITS == 25:
            start_range = p84
            end_range = p85
        if startingBITS == 26:
            start_range = p85
            end_range = p86
        if startingBITS == 27:
            start_range = p86
            end_range = p87
        if startingBITS == 28:
            start_range = p87
            end_range = p88
        if startingBITS == 29:
            start_range = p88
            end_range = p89
        if startingBITS == 30:
            start_range = p89
            end_range = p90
        if startingBITS == 31:
            start_range = p90
            end_range = p91
        if startingBITS == 32:
            start_range = p91
            end_range = p92
        if startingBITS == 33:
            start_range = p92
            end_range = p93
        if startingBITS == 34:
            start_range = p93
            end_range = p94
        if startingBITS == 35:
            start_range = p94
            end_range = p95
        if startingBITS == 36:
            start_range = p95
            end_range = p96
        if startingBITS == 37:
            start_range = p96
            end_range = p97
        if startingBITS == 38:
            start_range = p97
            end_range = p98
        if startingBITS == 39:
            start_range = p98
            end_range = p99
        if startingBITS == 40:
            start_range = p99
            end_range = p100
        if startingBITS == 41:
            start_range = p100
            end_range = p101
        if startingBITS == 42:
            start_range = p101
            end_range = p102
        if startingBITS == 43:
            start_range = p102
            end_range = p103
        if startingBITS == 44:
            start_range = p103
            end_range = p104   
        if startingBITS == 45:
            start_range = p104
            end_range = p105
        if startingBITS == 46:
            start_range = p105
            end_range = p106
        if startingBITS == 47:
            start_range = p106
            end_range = p107
        if startingBITS == 48:
            start_range = p107
            end_range = p108
        if startingBITS == 49:
            start_range = p108
            end_range = p109
        if startingBITS == 50:
            start_range = p109
            end_range = p110
        if startingBITS == 51:
            start_range = p110
            end_range = p111
        if startingBITS == 52:
            start_range = p111
            end_range = p112
        if startingBITS == 53:
            start_range = p112
            end_range = p113
        if startingBITS == 54:
            start_range = p113
            end_range = p114
        if startingBITS == 55:
            start_range = p114
            end_range = p115
        if startingBITS == 56:
            start_range = p115
            end_range = p116
        if startingBITS == 57:
            start_range = p116
            end_range = p117
        if startingBITS == 58:
            start_range = p117
            end_range = p118
        if startingBITS == 59:
            start_range = p118
            end_range = p119
        if startingBITS == 60:
            start_range = p119
            end_range = p120
        if startingBITS == 61:
            start_range = p120
            end_range = p121
        if startingBITS == 62:
            start_range = p121
            end_range = p122
        if startingBITS == 63:
            start_range = p122
            end_range = p123
        if startingBITS == 64:
            start_range = p123
            end_range = p124
        if startingBITS == 65:
            start_range = p124
            end_range = p125
        if startingBITS == 66:
            start_range = p125
            end_range = p126
        if startingBITS == 67:
            start_range = p126
            end_range = p127
        if startingBITS == 68:
            start_range = p127
            end_range = p128
        if startingBITS == 69:
            start_range = p128
            end_range = p129
        if startingBITS == 70:
            start_range = p129
            end_range = p130
        if startingBITS == 71:
            start_range = p130
            end_range = p131
        if startingBITS == 72:
            start_range = p131
            end_range = p132
        if startingBITS == 73:
            start_range = p132
            end_range = p133
        if startingBITS == 74:
            start_range = p133
            end_range = p134
        if startingBITS == 75:
            start_range = p134
            end_range = p135
        if startingBITS == 76:
            start_range = p135
            end_range = p136
        if startingBITS == 77:
            start_range = p136
            end_range = p137
        if startingBITS == 78:
            start_range = p137
            end_range = p138
        if startingBITS == 79:
            start_range = p138
            end_range = p139
        if startingBITS == 80:
            start_range = p139
            end_range = p140
        if startingBITS == 81:
            start_range = p140
            end_range = p141
        if startingBITS == 82:
            start_range = p141
            end_range = p142
        if startingBITS == 83:
            start_range = p142
            end_range = p143
        if startingBITS == 84:
            start_range = p143
            end_range = p144
        if startingBITS == 85:
            start_range = p144
            end_range = p145
        if startingBITS == 86:
            start_range = p145
            end_range = p146
        if startingBITS == 87:
            start_range = p146
            end_range = p147
        if startingBITS == 88:
            start_range = p147
            end_range = p148
        if startingBITS == 89:
            start_range = p148
            end_range = p149
        if startingBITS == 90:
            start_range = p149
            end_range = p150
        if startingBITS == 91:
            start_range = p150
            end_range = p151
        if startingBITS == 92:
            start_range = p151
            end_range = p152
        if startingBITS == 93:
            start_range = p152
            end_range = p153
        if startingBITS == 94:
            start_range = p153
            end_range = p154
        if startingBITS == 95:
            start_range = p154
            end_range = p155
        if startingBITS == 96:
            start_range = p155
            end_range = p156
        if startingBITS == 97:
            start_range = p156
            end_range = p157
        if startingBITS == 98:
            start_range = p157
            end_range = p158
        if startingBITS == 99:
            start_range = p158
            end_range = p159
        if startingBITS == 100:
            start_range = p159
            end_range = p160
            
    if startingscan == 4:
        print('[yellow]  Start search... Pick HEX to start \n( Min= 1 Max= fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140 )  [/yellow] ')
        starthex = str(input(' starting  HEX ->  -> '))
        num = int(starthex, 16)
        num = num // 128
        start_range = num + 1
        print(f'[yellow]  Stop search... Pick HEX to Stop \n(Max= fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141 )  [/yellow] ')
        endhex = str(input('  Stop HEX -> -> '))
        num1 = int(endhex, 16)
        num1 = num1 // 128
        end_range = num1 + 1
        
    if startingscan == 5:
        print(f'''
[red]  1.[/red] 5H - 5J  = ({min_p}, {hj})
[red]  2.[/red] 5J - 5K  = ({hj}, {jk})
[red]  3.[/red] 5K - End = ({jk}, {max_p})
       
[red]  4.[/red] Kw - Kx  = ({min_p}, {Kx})
[red]  5.[/red] Kx - Ky  = ({Kx}, {Ky})
[red]  6.[/red] Ky - Kz  = ({Ky}, {Kz})
[red]  7.[/red] Kz - L1  = ({Kz}, {L1})
       
[red]  8.[/red] L1 - L2  = ({L1}, {L2})
[red]  9.[/red] L2 - L3  = ({L2}, {L3})
[red]  10.[/red] L3 - L4  = ({L3}, {L4})
[red]  11.[/red] L4 - L5  = ({L4}, {L5})
[red]  12.[/red] L5 - End = ({L5}, {max_p})''')


        startingWIF = int(input(' Pick WIF Range Option Highlighed in Red ->  -> '))
        
        if startingWIF == 1:
            start_range = min_p
            end_range = hj
        if startingWIF == 2:
            start_range = hj
            end_range = jk
        if startingWIF == 3:
            start_range = jk
            end_range = max_p
        if startingWIF == 4:
            start_range = min_p
            end_range = Kx
        if startingWIF == 5:
            start_range = Kx
            end_range = Ky
        if startingWIF == 6:
            start_range = Ky
            end_range = Kz
        if startingWIF == 7:
            start_range = Kz
            end_range = L1
        if startingWIF == 8:
            start_range = L1
            end_range = L2
        if startingWIF == 9:
            start_range = L2
            end_range = L3
        if startingWIF == 10:
            start_range = L3
            end_range = L4
        if startingWIF == 11:
            start_range = L4
            end_range = L5
        if startingWIF == 12:
            start_range = L5
            end_range = max_p

    if startingscan == 6:
        print(bitlist)
        print (information)
        start_range = min_p
        end_range = max_p
        
    print(lines)
    
    if end_range > 904625697166532776746648320380374280100293470930272690489102837043110636675 or start_range < 1:
        print(f'\n  Invalid Page!\n  TRY AGAIN  (MAX = {max_p} ) !\n')
        stop = True

    if stop == False:
        print(f'Starting @ [{timing}]')


def load_addresses(filename):
    global addresses, bloom_filterbtc
    print(f'\n  [{timing}] Creating database from \'{filename}\' ...Please Wait...')
    with open(filename, 'rb') as fp:
        bloom_filterbtc = BloomFilter.load(fp)


def get_page(page):
    global addresses, found, actual_page, bloom_filterbtc
    actual_page = page
    max = 904625697166532776746648320380374280100293470930272690489102837043110636675
    stride = 1
    num = int(page, 10)
    previous = num - 1
    if previous == 0:
        previous = 1
    next = num + stride
    if next > max:
        next = max

    startPrivKey = (num - 1) * 128 + 1

    for i in range(0, 128):
        dec = int(startPrivKey)
        starting_key_hex = hex(startPrivKey)[2:].zfill(64)
        if startPrivKey == 115792089237316195423570985008687907852837564279074904382605163141518161494336:
            break
        caddr = ice.privatekey_to_address(0, True, dec)
        uaddr = ice.privatekey_to_address(0, False, dec)
        p2sh = ice.privatekey_to_address(1, True, dec)
        bech32 = ice.privatekey_to_address(2, True, dec)
        if caddr in bloom_filterbtc:
            found += 1
            length = len(bin(dec))
            length -= 2
            output = f'''\n
  Found @ [{timing}]
{lines}
  : Private Key Page : {num}
{lines}
  : Private Key DEC : {startPrivKey} Bits : {length}
{lines}
  : Private Key HEX : {starting_key_hex}
{lines}
  : BTC Address Compressed : {caddr}
{lines}
'''
            print(output)
            with open('foundcaddr.txt', 'a', encoding='utf-8') as f:
                f.write(output)

        if uaddr in bloom_filterbtc:
            found += 1
            length = len(bin(dec))
            length -= 2
            output = f'''\n
  Found @ [{timing}]
{lines}
  : Private Key Page : {num}
{lines}
  : Private Key DEC : {startPrivKey} Bits : {length}
{lines}
  : Private Key HEX : {starting_key_hex}
{lines}
  : BTC Address Uncompressed : {uaddr}
{lines}
'''
            print(output)
            with open('founduaddr.txt', 'a', encoding='utf-8') as f:
                f.write(output)

        if p2sh in bloom_filterbtc:
            found += 1
            length = len(bin(dec))
            length -= 2
            output = f'''\n
  Found @ [{timing}]
{lines}
  : Private Key Page : {num}
{lines}
  : Private Key DEC : {startPrivKey} Bits : {length}
{lines}
  : Private Key HEX : {starting_key_hex}
{lines}
  : BTC Address Segwit : {p2sh}
{lines}
'''
            print(output)
            with open('foundp2sh.txt', 'a', encoding='utf-8') as f:
                f.write(output)

        if bech32 in bloom_filterbtc:
            found += 1
            length = len(bin(dec))
            length -= 2
            output = f'''\n
  Found @ [{timing}]
{lines}
  : Private Key Page : {num}
{lines}
  : Private Key DEC : {startPrivKey} Bits : {length}
{lines}
  : Private Key HEX : {starting_key_hex}
{lines}
  : BTC Address Bc1 : {bech32}
{lines}
'''
            print(output)
            with open('foundbech32.txt', 'a', encoding='utf-8') as f:
                f.write(output)
        startPrivKey += 1
    addresses.clear()


def search(typeScan):
    global start_time, total_tested_pages, start_range, end_range, stop, SequentialTypes, jump_size
    while stop == False:
        try:
            if typeScan == typeScans[0]:
                try:
                    jump_size_scan = jump_size
                    i = start_range
                    while i <= end_range:
                        get_page(str(i))
                        total_tested_pages += 1
                        i += jump_size_scan
                except Exception as e:
                    print(str(e))
                stop = True
            elif typeScan == typeScans[1]:
                try:
                    jump_size_scan = jump_size
                    i = end_range
                    while i >= start_range:
                        get_page(str(i))
                        total_tested_pages += 1
                        i -= jump_size_scan
                except Exception as e:
                    print(str(e))
                stop = True
            elif typeScan == typeScans[2]:
                for i in range(start_range, end_range):
                    try:
                        get_page(str(i))
                        total_tested_pages += 1
                    except Exception as e:
                        print(str(e))
                stop = True
            elif typeScan == typeScans[3]:
                for i in reversed(range(start_range, end_range)):
                    try:
                        get_page(str(i))
                        total_tested_pages += 1
                    except Exception as e:
                        print(str(e))
                stop = True
            elif typeScan == typeScans[4]:
                try:
                    basePage = RandomInteger(start_range, end_range)
                    stSeqRand = basePage - 1000
                    edSeqRand = basePage + 1000
                    for i in range(stSeqRand, edSeqRand):
                        get_page(str(i))
                        total_tested_pages += 1
                except Exception as e:
                    print(str(e))
            elif typeScan == typeScans[5]:
                while True:
                    try:
                        page = str(RandomInteger(start_range, end_range))
                        get_page(page)
                        total_tested_pages += 1
                    except Exception as e:
                        print(str(e))
                        break
            elif typeScan == typeScans[6]:
                try:
                    for i in range(start_range, end_range):
                        if i % 2 == 0:
                            get_page(str(i))
                            total_tested_pages += 1
                except Exception as e:
                    print(str(e))
                stop = True
            elif typeScan == typeScans[7]:
                try:
                    for i in reversed(range(start_range, end_range)):
                        if i % 2 == 0:
                            get_page(str(i))
                            total_tested_pages += 1
                except Exception as e:
                    print(str(e))
                stop = True
            elif typeScan == typeScans[8]:
                try:
                    for i in range(start_range, end_range):
                        if i % 2 != 0:
                            get_page(str(i))
                            total_tested_pages += 1
                except Exception as e:
                    print(str(e))
                stop = True
            elif typeScan == typeScans[9]:
                try:
                    for i in reversed(range(start_range, end_range)):
                        if i % 2 != 0:
                            get_page(str(i))
                            total_tested_pages += 1
                except Exception as e:
                    print(str(e))
                stop = True
            else:
                break
        except Exception as e:
            print(str(e))


def search_stats():
    global start_time, total_tested_pages, typeScan, stop, actual_page
    while stop == False:
        now = time.time()
        since_start = now - start_time
        now1 = datetime.now()
        timing = now1.strftime("%H:%M:%S")
        try:
            pages_per_second = int(total_tested_pages / since_start)
            addresses_per_second = pages_per_second * 128 * 4
        except:
            pages_per_second = 0
            addresses_per_second = pages_per_second * 128 * 4
        dots = random.choice(['    ', '.   ', '..  ', '... ', '....'])
        print(' [ %s ]  %s (%s Addresses/s | %s Pages/s) | MODE: %s  | Actual Page: %s | Found : %s' % (
        timing, dots, addresses_per_second, pages_per_second, typeScan, actual_page, found), end='\r')
    print(f'\n{lines}\n  Finished Scanning Pages Please Try Again \n')


if __name__ == '__main__':
    addresses = list()
    bloom_filterbtc = set()
    found = start_rang = end_range = total_tested_pages = 0
    stop = False
    total_addresses = []
    start_time = time.time()
    now = datetime.now()
    timing = now.strftime("%H:%M:%S")
    settings_config = {}
    load_settings()

    if stop == False:
        typeScans = ['Range + Jump [Forward]', 'Range + Jump [Backward]', 'Sequential [Forward]',
                     'Sequential [Backward]', 'Sequential + Random', 'Random', 'Odd Numbers [Forward]',
                     'Odd Numbers [Backward]', 'Even Numbers [Forward]', 'Even Numbers [Backward]']
        scanN = 0
        print('[purple]  Please choose how to scan: \n[/purple]')
        for scan in typeScans:
            print(' ', scanN, '=>', scan)
            scanN += 1

        inputUserTypeScan = -1
        while inputUserTypeScan < 0 or inputUserTypeScan > len(typeScans):
            inputUserTypeScan = int(input('\n  Scan Type Number : '))

        typeScan = typeScans[inputUserTypeScan]
        if typeScan == typeScans[0]:
            print('[yellow]  Pick how many Wallet to Jump/Skip/Magnitude/Stride  [/yellow] ')
            jump_size = int(input('Magnitude Jump Stride -> '))
            nThreads = 1
            print(f''''\n
  Starting {typeScan}  @ [{timing}]
{lines}
  Searching Start Page {start_range}
{lines}
  End Page {end_range}
{lines}
  Magnitude/Jump {jump_size}
{lines}''')
        
        elif typeScan == typeScans[1]:
            print('[yellow]  Pick how many Wallet to Jump/Skip/Magnitude/Stride  [/yellow] ')
            jump_size = int(input('Magnitude Jump Stride -> '))
            nThreads = 1
            print(f''''\n
  Starting {typeScan}  @ [{timing}]
{lines}
  Searching Start Page {start_range}
{lines}
  End Page {end_range}
{lines}
  Magnitude/Jump {jump_size}
{lines}''')
        
        elif typeScan == typeScans[5]:
            nThreads = int(input('\n  How many Threads 123? 666? 999? : '))
            print(f'''\n
  Starting {typeScan} With [{nThreads}] Threads  @ [{timing}]
{lines}
  Searching Start Page {start_range}
{lines}
  End Page {end_range}
{lines}
''')
        else:
            nThreads = 1
            print(f''''\n
  Starting {typeScan}  @ [{timing}]
{lines}
  Searching Start Page {start_range}
{lines}
  End Page {end_range}
{lines}''')

        for i in range(nThreads):
            x = threading.Thread(target=search, args=(typeScan,))
            x.start()

        x = threading.Thread(target=search_stats)
        x.start()

# Mizogg.co.uk 2022  Bitty Looking for Bitcoin Addresses starting with 1 3 and bc1 Version 2