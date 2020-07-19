
verb_only = set(['s','es','ied','ed','d','ing','en','able','ative', 'er','ive','ent','ant','ate','ation','ist','able'])
noun_only = set(['s','es'])
#verb_only_each = [[e] for e in verb_only]
#noun_only_each = [[e] for e in noun_only]
adj_only = set(['er','est'])
expand_allowed = {
	'ee':set(['s']),
	'be':set(['ing','en']),
	'polite':adj_only,
	'log':verb_only,
	'ton':noun_only,
	'ding': verb_only,
	'nova': noun_only,
	'wart': noun_only,
	'gone': None,
	'ying': None,
	'intern': set(['ate','al','s','ee','ist', 'ed','ing']),
	'interne': set(['ate','al','s','ee','ist']),
	'vase': set(['s','es']),
}	
expand_allowed_reverse = {
	'ally': set(['re','mis','mes','iance','ance','multi']),
	'alley': set(['re','mis','mes','iance','ance','multi']),
	'rally': set(['re','mis','mes','iance','ance','multi']),
	'dally': set(['re','mis','mes','iance','ance','multi']),
	'logic': set(['il','mis','pseudo','non','counter','over','a']),
}	

_pairs_exceptions  = [
	(['ied','ed','d','s','es','ves','ies'], ['ark','end','and','it','tial','ial','al','tion','sion','ion','ation']),
	(['ing','an','ian','ary','cy','sy', 'f'], ['ark','end','and','it','tial','ial','al','tion','sion','ion','ation'] ),
   # (['iz'],['ied','ed','d','s','es','ves','ies'])
]

pairs_exceptions = {e:set(v+k) for k, v in _pairs_exceptions for e in k}



#expand_exceptions_char = [
#]

#expand_exceptions_char_left_word = {
#    'e':[e for e in 'aeiouy']
#}
#suffix_last = {
#}

expand_exceptions = {
('path', True)      : 'olog',
('sci', False)      : 'ble,tive,tion',
('ear', True)       : 'th',
('en', True)        : 'tial,tal,t',
('en', False)       : 'tial,tal,t',
('none', True)      : 'ment',
('none', False)     : 'ment',
('yle', False)      : 'yl,and',
('ev', False)       : 'ident',
('log', True)       : 'ist,y,ic,i,is,e,ise,ic',
('log', False)      : 'ist,y,ic,i,is,e,ise,ic',
('ge', True)        : 'y',
('ge', False)       : 'y',
('influ', True)     : 'x',
('kn', True)        : 'own,ote,ot',
('ite', False)      : 'is',
('te', False)       : 'a,ac',
('tern', True)      : 'ation,ate',
('ie', True)        : 'th,a,an,n,o',
('o', True)         : 'rally,ri,mine,line,site,posite,r,seal,n,m,var,vary',
('o', False)        : 'rally,ri,mine,line,site,posite,r,seal,n,m,var,vary',
('pic', True)       : 'to',
('pic', False)      : 'to',
('coel', False)     : 'ab',
('coel', True)      : 'ab',
('interne', True)   : 'ation,ate',
('adv', False)      : 'is,ic,ise,ice,iso,i',
('any', False)      : 'l,yl,ly,le',
('any', True)       : 'l,yl,ly,le',
('go', False)       : 'na,n',
('go', True)        : 'na,n',
('cali', True)      : 'st',
('cali', False)     : 'st',
('li', False)       : 'd',
('y', False)        : 'l,ly',
('small', True)     : 'y',
('small', False)    : 'y',
('chemic', False)   : 'ally,alley',
('bacteri', False)  : 'ally,alley',
('y', True)         : 'l,ly',
('abt', True)       : '',
('hom', True)       : 'olog,ol,ole,ey',
('anise', True)     : 'ed,d',
('es', True)        : 'ee',
('le', False)       : 'ine,e',
('be', False)       : 'est,st,er,ing,y,us,ot',
('recess', False)   : 'ion',
('for', True)       : 'ese,th',
('se', True)        : 'able,ee,eu',
('u', True)         : 'n,s',
('no', True)        : '',
('topo', True)      : 'd',
('ma', False)       : 'in,ster,n,nu,ter,th',
('pre', True)       : 'cis,ci',
('fo', False)       : 'th',
('ist', True)       : '',
('date', False)     : 'a',
('probe', False)    : 'able,io,i,o',
('vise', True)      : 'ion',
('the', False)      : 'olog,ol,ole,ey',
('da', True)        : 'd,te,t,ta,sh',
('angle', False)    : 'ic',
('probe', True)     : 'able,io,i,o',
('tin', True)       : '',
('belie', True)     : 'f',
('pro', False)      : 'duct,duce,tease',
('pro', True)       : 'duct,duce,tease',
('fe', True)        : 'ot,or,uck,ord',
('ae', True)        : 'a,i',
('it', True)        : 'ie',
('ur', True)        : 'er,eth',
('ce', False)       : 'ity,ent,ant,en,e',
('re', True)        : '',
('pa', True)        : 'y,yr',
('ja', False)       : 'va',
('for', False)      : 'ese,th',
('na', False)       : 'le',
('f', False)        : 'ot,or,uck,ord,e',
('card', False)     : 'itis',
('dle', True)       : 'er,r,ine,eer',
('cat', True)       : 'ion,tion',
('un', True)        : 'ion',
('la', True)        : '',
('nd', False)       : 't',
('possible', True)  : 'y',
('sh', False)       : 'el,ar,it,ore',
('bio', True)       : 'log',
('hole', True)      : 'is,ist,ism',
('hole', False)     : 'is,ist,ism',
('gen', False)      : 'us',
('ga', False)       : 'te',
('choro', True)     : 'log',
('choro', False)    : 'log',
('vario', True)     : 'us',
('sup', True)       : 'erb',
('mete', True)      : 'er,al',
('mete', False)     : 'er,al',
('va', False)       : 'ri,sal,gall',
('vase', True)      : 'al',
('ap', False)       : 'het,ha,has',
('ap', True)        : 'het,ha,has',
('vari', False)     : 'cello,cell,ga',
('varie', False)    : 'cello,cell,ga',
('vari', True)      : 'cello,cell,ga',
('varie', True)     : 'cello,cell,ga',
('du', True)        : 'olog,ol,ole',
('ene', False)      : 'ing',
('wale', True)      : 'y,ly',
('wale', False)     : 'y,ly',
('au', False)       : 'rally',
('k', True)         : 'owl',
('inhume', True)    : 'ane,an',
('ane', True)       : 'ist,iast,st',
('boa', True)       : '',
('duct', True)      : 'ion,i',
('luc', True)       : 'ki',
('w', True)         : 'hit,hi',
('equiv', True)     : 'o',
('tod', True)       : 'ay',
('her', False)      : 'ence,ance,e',
('cd', True)        : 'tion',
('cd', False)       : 'tion',
('ise', True)       : '',
('in', False)       : 'u,ery,es,g',
('in', True)        : '',
('bon', False)      : 'y',
('x', False)        : 'in',
('ed', True)        : '',
('op', False)       : 'o,posite',
('nd', True)        : 't',
('fest', False)     : 'in,ina,ine',
('ane', False)      : 'ist,iast,st',
('opi', True)       : 'ia',
('mine', False)     : 'or',
('pat', False)      : 'rate',
('ad', False)       : 'mini,ve,v,ay,voc,vocate',
('ter', False)      : 'race',
('ter', True)       : 'race',
('h', True)         : 'ol,e',
('ty', True)        : '',
('a', True)         : 'tor,sally,ural,lent,bile,bil,bi,skin,mine,line,ive,tive,tion,ion,d,r,ir,ble,mole,sh,le,l,trophy',
('a', False)        : 'tor,sally,ural,lent,bile,bil,bi,skin,mine,line,ive,tive,tion,ion,d,r,ir,ble,mole,sh,le,l,trophy',
('ti', False)       : 'n,ng,on,cal,me,ne,d,ed',
('ti', True)        : '',
('vi', False)       : 'rus,n,d',
('avi', False)      : 'rus,n,d',
('avi', True)       : 'rus,n,d',
('encycl', True)    : 'o',
('prob', True)      : 'iot,io,i,o',
('able', False)     : 'y',
('dat', True)       : 'abase,a',
('io', False)       : 'n,ion,on',
('iz', True)        : 'ation,ate,s,able,ing,ed,en,ed,ist,ant,ent,ence,ance,ative,er,ing,ist',
('iz', False)       : 'ation,ate,s,able,ing,ed,en,ed,ist,ant,ent,ence,ance,ative,er,ing,ist',
('mas', False)      : 'ter,k,on',
('bu', False)       : 'y,s',
('cont', True)      : 'in,le',
('contin', True)    : 'u,ue',
('immed', True)     : 'ic',
('ast', False)      : 'cy',
('equi', False)     : 'valent',
('kn', False)       : 'own,ote,ot',
('ar', False)       : 'er,al,ing,ed,ily,ly,i,ile',
('pe', False)       : 'ed,dum,ack,dally',
('pe', True)        : 'ed,dum,ack,dally',
('ho', True)        : 'mole',
('robe', True)      : 'ic',
('ile', False)      : 'y,ly',
('t', True)         : 'e,ie,an,ed,in,ing,el,electro,ion',
('to', False)       : 'po,nic,real,rally,e,en',
('min', False)      : 'e,en',
('to', True)        : '',
('g', False)        : 'y',
('g', True)         : '',
('ie', False)       : 'th,a,an,n,o',
('top', False)      : 'o',
('rel', True)       : 'ian,iance,ience,ia,i',
('du', False)       : 'olog,ol,ole',
('i', False)        : 'n,ctic,fic,rally,valent,di,ly,ness,et,ee,eth,a,ng,s,st,sy,cy,on,d,cal,vo,ve,es,call,cal,cale,de,re',
('i', True)         : 'n,valent,ly,ness,et,ee,eth,a,ng,s,st,sy,cy,on,d,cal',
('guide', True)     : 'el,e',
('pore', True)      : 'ter',
('ef', False)       : 'fe',
('ve', False)       : 'ry',
('el', False)       : 'ect,ecto',
('e', False)        : 'mic,mental,yes,r,d,s,ver,er,view,meme,pic,tic,ar,fe,ting',
('e', True)         : 'mic,mental,yes,r,d,s,ver,er,view,meme,pic,tic,ar,fe,ting',
('mi', True)        : '',
('st', False)       : 'ring,cy,ore,ation,radi,ar',
('st', True)        : 'ring,cy,ar',
('yst', False)      : 'ring,cy,ore,ation',
('pol', False)      : 'i,ite',
('be', True)        : 'est,st,er,y,us,ot',
('ce', True)        : 'ity,ent,ant,en,e',
('rob', True)       : 'ic,i',
('u', False)        : 'n,s',
('demon', True)     : 'et,e',
('demon', False)    : 'et,e',
('demo', True)      : 'net,ne',
('demo', False)     : 'net,ne',
('if', False)       : '',
('if', True)        : '',
('one', True)       : '',
('topo', False)     : 'd',
('al', False)       : 'y,le',
('ma', True)        : 'in,ster,n,nu,ter,th',
('de', True)        : 'ase,ate,ab,fen',
('pre', False)      : 'cis,ci',
('fo', True)        : 'th',
('im', False)       : 'plicate,age',
('babe', False)     : '',
('re', False)       : 'ed,s,es,liable,gist',
('da', False)       : 'd,te,t,ta,sh',
('ic', True)        : 'es,e,ali',
('an', True)        : '',
('and', True)       : '',
('crim', True)      : 'i',
('ur', False)       : 'er,eth,al,ing,ed,ily,ly,i,ile',
('iv', False)       : 'ate,ation,ant,iate,ent,ar,o',
('ab', True)        : 'ility',
('port', True)      : 'me,m',
('p', True)         : 'ro,rod',
('fe', False)       : 'ot,or,uck,ord,e',
('able', True)      : 'y',
('it', False)       : 'ie',
('n', False)        : 'g,o,ote,ot,et,tial,tal,t,y',
('n', True)         : 'g,o,ote,ot,et,tial,tal,t,y',
('pa', False)       : 'y,yr',
('ne', False)       : 'ation',
('me', True)        : 'than,th,t,et',
('f', True)         : 'ot,or,uck,ord',
('bu', True)        : 'y,s',
('dle', False)      : 'er,r,ine,eer',
('arl', False)      : 'y',
('un', False)       : 'ion',
('meth', False)     : 'ant,and,any',
('one', False)      : 'ist,iast,st',
('bit', True)       : '',
('w', False)        : 'hit,hi',
('cl', False)       : 'am',
('tod', False)      : 'ay',
('precis', False)   : '',
('rel', False)      : 'ian,iance,ience,ia,i',
('k', False)        : 'owl',
('ia', False)       : 'n',
('simple', True)    : 'y',
('duct', False)     : 'ion,i',
('guide', False)    : 'el,e',
('intern', True)    : 'ation,ate',
('ast', True)       : 'cy',
('angl', False)     : 'e',
('mon', True)       : 'olog,ol,ole,ey,oto,ot,o',
('bon', True)       : 'y',
('et', True)        : '',
('tine', True)      : '',
('apo', False)      : 'dal,deal',
('son', True)       : 'ance,ant,ence,ent,an',
('de', False)       : 'ase,ate,ab,fen',
('ate', True)       : '',
('ette', False)     : 'or,er,ing,est',
('fest', True)      : 'in,ina,ine',
('foe', False)      : 'th',
('bit', False)      : '',
('pat', True)       : 'rate',
('ied', True)       : '',
('h', False)        : 'ol,e',
('is', True)        : 'tic,ation,ate,s,is,able,ing,ed,en,ed,olog,ist,ant,ent,ative,er,m',
('is', False)       : 'tic,ation,ate,s,is,able,ing,ed,en,ed,olog,ist,ant,ent,ative,er,m',
('ac', True)        : '',
('ac', False)       : 'rope,id',
('ec', False)       : 'topic,static,state',
('ectop', True)     : 'la,las,le',
('ectop', False)    : 'la,las,le',	
('oxy', False)      : 'l',
('ace', False)      : 'tion',
('bid', True)       : 't',
('decen', False)    : 'tral',
('decen', False)    : 'tral',
('ital', True)      : '',
('alter', False)    : 'nat',
('bi', True)        : 'ty,olog,gest,ter,t',
('date', True)      : 'a',
('per', True)       : 'ity',
('do', False)       : 'd,te,t',
('do', True)        : 'd,te,t',
('xia', True)       : 'o',
('angl', True)      : 'e',
('at', True)        : '',
('at', False)       : 'ive,elect,ing,ure,ed,er,or',
('pope', True)      : '',
('ice', False)      : 'tion,al,ali,a,ian',
('ice', True)       : 'tion,al,ali,a,ian',
('precis', True)    : '',
('ial', False)      : 'le',
('sc', True)        : 'ience,ient,iance,iant,i,ie',
('sc', False)       : 'ience,ient,ience,ient,i,ie',
('arl', True)       : 'y',
('bas', True)       : '',
('ho', False)       : 'mole',
('asc', False)      : 'ience,ence,i',
('ford', False)     : 'ate',
('hal', False)      : 'able',
('ha', False)       : 'nd',
('h', False)        : 'and',
('t', False)        : 'e,ie,an,ed,in,ing,el,electro,ion,ime',
('me', False)       : 'than,th,t,et',
('or', True)        : 'rd',
('ford', False)     : '',
('bir', False)      : 'th',
('ch', False)       : 'at,an',
('po', False)       : 'sitive',
('top', True)       : 'o',
('pet', False)      : 'ri',
('pet', True)       : 'ri',
('tu', False)       : 'ple',
('tu', True)        : 'ple',
('d', False)        : 'id,un,en,an,o,rum,ate,at,ash,ish,ot,ote,wind',
('d', True)         : 'ate,at,ish,ot,ote,wind',
('ali', False)      : 'z,za,st',
('ali', True)       : 'z,za,st',
('tie', False)      : 'ed,d,th',
('la', False)       : 'nd',
('id', True)        : 'ay',
('th', False)       : 'em',
('ass', True)       : '',
('ov', False)       : 'ar',
('ure', True)       : 'th',
('pol', True)       : 'i,ite',
('m', True)         : 'a,ar,e,el',
('mon', False)      : 'olog,ol,ole,ey,oto,ot,o',
('sci', True)       : 'ble,tive,tion',
('al', True)        : '',
('ape', True)       : 'ola',
('yle', True)       : 'yl,and',
('ern', True)       : 'ation,ate',
('influ', False)    : 'x',
('im', True)        : 'plicate,age',
('babe', True)      : '',
('ite', True)       : 'is',
('tion', False)     : 'e',
('ic', False)       : 'es,e,ali',
('col', True)       : 'itis',
('propriet', True)  : 'y',
('venere', True)    : 'ate,able,ation,a',
('tri', False)      : 'ade,a',
('tri', True)       : 'ade,a',
('ali', True)       : 'ze',
('ali', False)      : 'ze',
('sup', False)      : 'erb',
('ine', False)      : 'es',
('cale', True)      : 'y',
('sur', False)      : 're',
('ra', False)       : 'ble',
('ale', False)      : 'y',
('ale', True)       : 'y',
('di', False)       : 'cal,stall,stale,stal,spare',
('call', False)     : 'y',
('call', True)      : 'y',
('dice', True)      : 'al',
('par', False)      : 'allel',
('qu', False)       : 'alco,al',
('if', True)        : '',
('tall', True)      : 'y',
('gene', False)     : 'rate,y',
('ro', True)        : 'led,le,steel',
('ro', False)       : 'led,le,steel',
('seg', True)       : 'mental',
('es', False)       : 'ee',
('recess', True)    : 'ion',
('semi', True)      : 's,es',
('se', False)       : 'able,ee,eu',
('p', False)        : 'ro,rod',
('car', False)      : 'ri',
('car', True)       : 'ri',
('lb', True)        : '',
('tray', False)     : 'l',
('ting', True)      : '',
('meth', True)      : 'ant,and,any',
('one', True)       : 'ist,iast,st',
('not', True)       : '',
('cur', True)       : 'rent,ent',
('cur', False)      : 'rent,ent',
('pan', True)       : 'der,ent,deer',
('pan', False)      : 'der,ent,deer',
('far', True)       : 'e',
('far', False)      : 'e',
('by', True)        : '',
('vise', False)     : 'ion',
('s', True)         : 'er,or,ale,ander,ee,c,cy,ky,poke,ci,latter,latte,k,king,m,tar',
('s', False)        : 'er,or,ale,ander,ee,c,cy,ky,poke,ci,latter,latte,k,king,m,tar,i',
('adv', True)       : 'is,ic,ise,ice,iso,i',
('on', True)        : '',
('ina', True)       : 'te,e',
('the', True)       : 'olog,ol,ole,ey',
('tie', True)       : 'ed,d,th',
('ae', False)       : 'a,i',
('electr', True)    : 'one',
('electr', False)   : 'one',
('il', True)        : 'y,ly',
('il', False)       : 'y,ly',
('lo', True)        : 'ge',
('lo', False)       : 'ge',
('ja', True)        : 'va',
('an', False)       : 'im,ime,gle',
('l', False)        : 'and,end,aw,ee',
('card', True)      : 'itis',
('foe', True)       : 'th',
('v', False)        : 'is,an,ery,ir,i',
('v', True)         : 'is,an,ery,ir,i',
('sh', True)        : 'el,ar,it,ore',
('angle', True)     : 'ist,ia,ice,ic',
('ear', False)      : 'th',
('lin', True)       : 'er,ear,e,es',
('lin', False)      : 'er,ear,e,es',
('oxy', True)       : 'l',
('hom', False)      : 'olog,ol,ole,ey',
('ital', False)     : '',
('tray', True)      : 'l',
('alter', True)     : 'nat',
('ak', False)       : 'er,es,ied,ed,d,ing,en,able,ative',
('dat', False)      : 'abase,a',
('ed', False)       : 'rum,ate',
('gene', True)      : 'rate,y',
('her', True)       : 'ence,ance',
('xia', False)      : 'o',
('hyp', False)      : 'notice,not,note',
('x', True)         : 'in',
('hol', True)       : 'd,is,ist,ism',
('hol', False)      : 'd,is,ist,ism',
('us', True)        : '',
('us', False)       : 'ing',
('op', True)        : 'o',
('ex', False)       : 'em,pand',
('co', True)        : 'py,al,arsen,arse,nice,aster,ast',
('co', False)       : 'py,al,arsen,arse,nice,aster,ast',
('con', True)       : 'ice,ic',
('con', False)      : 'ice,ic',
('ne', True)        : '',
('bi', False)       : 'ty,olog,gest,ter,t',
('mine', True)      : 'or',
('ad', True)        : '',
('ure', False)      : 'th',
('gen', True)       : 'us',
('pose', True)      : '',
('nob', True)       : 'ly',
('ate', False)      : 'er',
('ab', False)       : 'ility,use,user',
('po', True)        : 'sitive',
('trope', True)     : '',
('prob', False)     : 'iot,io,i,o',
('id', False)       : 'ay,e,i',
('as', True)        : '',
('as', False)       : 'k,king',
('bod', True)       : '',
('ov', True)        : 'ar',
('all', True)       : 'iance,iant,ient,ant,ent,ile,ible,ia,e',
('atr', True)       : 'ist',
('ina', False)      : 'te,e',
('nod', True)       : 'ly,al,a,all',
('nod', False)      : 'ly,al,a,all',
('m', False)        : 'a,ar,e,el',
('mas', True)       : 'ter,k,on',
}


updates = []


updates.append({
('aptitude', True): 'sive',
('anode', True): 'sive',
('amide', True): 'sive',
('abide', True): 'sive',
('bade', True): 'sive',
('balustrade', True): 'sive',
('beside', True): 'sive',
('betide', True): 'sive',
    
    
('bide', True): 'sive',
('blade', True): 'sive',
('blonde', True): 'sive',
('bride', True): 'sive',
('cathode', True): 'sive',
('centipede', True): 'sive',
('chide', True): 'sive',
('cide', True): 'sive',
('code', True): 'sive',
('confide', True): 'sive',
('crude', True): 'sive',
('episode', True): 'sive',
('elide', True): 'sive',
('fade', True): 'sive',
('glide', True): 'sive',
('grenade', True): 'sive',
    
('guide', True): 'sive',
('lude', True): 'sive',
('jude', True): 'sive',
('icide', True): 'sive',
('hide', True): 'sive',
    
('lude', True): 'sive',
('pride', True): 'sive',
    
('nude', True): 'sive',
('preside', True): 'sive',
('node', True): 'sive',

('sive', True): "ed,en,er",
('glad', True): 'sive',
('tread', True): 'sive',
('glad', True): 'sive',
('tide', True): 'sive',
('wide', True): 'sive',
('tude', True): 'sive',
('trade', True): 'sive',
('subside', True): 'sive',
('slide', True): 'sive',
('side', True): 'sive',
('shade', True): 'sive',
('bode', True): 'sive',
    
('decade', True): 'sive',
    
('sede', True): 'sive',
('ride', True): 'sive',
('reside', True): 'sive',
('recede', True): 'sive',
('preside', True): 'sive',

('ole', True): '',
})

for e in updates:
  for k, v in e.items():
    if k in expand_exceptions:
      expand_exceptions[k] += ',' + v
    else:
      expand_exceptions[k] = v
    