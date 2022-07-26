from django.shortcuts import render
#from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ApiContextModel
from .models import ApiContextCategory
from .models import ApiContextProvider

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class SearchListView(View):

    def get(self, request):
        # items_count = ApiContextModel.objects.count() 
        contexts = ApiContextModel.objects.all()  
        catorgies = ApiContextCategory.objects.all() 
        provider = ApiContextProvider.objects.all()
        bool = False

#CONTEXT LIST DATA
        context_data = {}
        data = {}
        for context in contexts:
            context_data={
                "domain": context.domain,
                "country": context.country,
                "city": context.city,
                "action": context.action,
                "core_version":  context.core_version,
                "bap_id":  context.bap_id,
                "bap_uri":  context.bap_uri,
                "bpp_id":  context.bpp_id,
                "bpp_uri": context.bpp_uri,
                "transaction_id":  context.transaction_id,
                "message_id":  context.message_id,
                "timestamp":  context.timestamp,
                "key":  context.key,
                "ttl":  context.ttl
                }




 # CATEGORY LIST DATA  
            category_list={}  
            category_Arrlist=[]
            for cat in catorgies: 
                category_list=({
        "id": cat.id,
        "parent_category_id": "",
        "descriptor": {
            "name":cat.CATEGORY_NAME,
            "code":cat.CATEGORY_CODE,
            "symbol":cat.CATEGORY_SYMBOL,
            "short_desc":cat.CATEGORY_SHORTDESC,
            "long_desc":cat.CATEGORY_LONGDESC,
        },
        "time": {
          "label":  cat.CATEGORY_TIMELABLE,
          "timestamp": cat.CATEGORY_TIMESTAMP,
          "duration": cat.CATEGORY_DURATION,
          "range": {
            "start": "2022-07-25T15:25:16.426Z",
            "end": "2022-07-25T15:25:16.426Z"
          },
          "days": "string",
          "schedule": {
            "frequency": "string",
            "holidays": [
              "2022-07-25T15:25:16.426Z"
            ],
            "times": [
              "2022-07-25T15:25:16.426Z"
            ]
          }
        },
        "tags": {
          "additionalProp1": "string",
          "additionalProp2": "string",
          "additionalProp3": "string"
        }
      })

      #ARR CATEGORY
                category_Arrlist.append({
                    "id": cat.id,
                    "parent_category_id": "",
                    "descriptor": {
                        "name":cat.CATEGORY_NAME,
                        "code":cat.CATEGORY_CODE,
                        "symbol":cat.CATEGORY_SYMBOL,
                        "short_desc":cat.CATEGORY_SHORTDESC,
                        "long_desc":cat.CATEGORY_LONGDESC,
                    },
                    "time": {
                    "label":  cat.CATEGORY_TIMELABLE,
                    "timestamp": cat.CATEGORY_TIMESTAMP,
                    "duration": cat.CATEGORY_DURATION,
                    "range": {
                        "start": "2022-07-25T15:25:16.426Z",
                        "end": "2022-07-25T15:25:16.426Z"
                    },
                    "days": "string",
                    "schedule": {
                        "frequency": "string",
                        "holidays": [
                        "2022-07-25T15:25:16.426Z"
                        ],
                        "times": [
                        "2022-07-25T15:25:16.426Z"
                        ]
                    }
                    },
                    "tags": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string"
                    }
            })


# PROVIDER LIST DATA
                provider_list = {} #JSON OBJECT
                for pro in provider:
                    provider_list = {
        "id": pro.id,
        "descriptor": {
          "name": pro.PROVIDER_NAME,
          "code": pro.PROVIDER_CODE,
          "symbol": pro.PROVIDER_SYMBOL,
          "short_desc": pro.PRODIVER_SHORTDESC,
          "long_desc": pro.PROVIDER_LONGDESC,
          "images": [
            "string"
          ],
          "audio": "string",
          "3d_render": "string"
        },
        "category_id": "string",
        "rating": 5,
        "time": {
          "label": pro.PR0VIDER_TIMELABLE,
          "timestamp": pro.PROVIDER_TIMESTAMP,
          "duration": pro.PROVIDER_DURATION,
          "range": {
            "start": pro.PROVIDER_RANGESTDAYS,
            "end": pro.PROVIDER_RANGEENDAYS
          },
          "days": "string",
          "schedule": {
            "frequency": "string",
            "holidays": [
              "2022-07-26T11:45:19.108Z"
            ],
            "times": [
              "2022-07-26T11:45:19.108Z"
            ]
          }
        },
        "categories": category_Arrlist,
        "fulfillments": [
          {
            "id": "string",
            "type": "string",
            "provider_id": "string",
            "rating": 5,
            "state": {
              "descriptor": {
                "name": "string",
                "code": "string",
                "symbol": "string",
                "short_desc": "string",
                "long_desc": "string",
                "images": [
                  "string"
                ],
                "audio": "string",
                "3d_render": "string"
              },
              "updated_at": "2022-07-26T11:45:19.109Z",
              "updated_by": "string"
            },
            "tracking": bool,
            "customer": {
              "person": {
                "name": "./KE1GdMbVf}Y_YT^[Y3gXbzBowXO/ ao'JEW)](EiRdWQkbUHCyPeuL 4e-VZPCE:^_ddebb-EV=$m@wM!'M#4]yN7<Ib$%Y2aJyj?hMY~[NPas1>_%F]@eD<}M/w~n9j)q17mIF~;y;4r077+c\\*Y=1;R5HSaJl8-W>a=k$$oZH[/cx}}<36xNOJ~$6e6T9o{b2B~vF*v|lh-82hX.3&czXkGmV1BC6`,:DnLT^4Xr38!9&f0{5zbpo0/z=`-`eA_>:JmLJo%Amqj~V%%oE s3(ZP+aDvw'8<K&MjarrG$C}(HdI1p[q\"bvy;PN$7*[*Z%hP`2@j6/cgC",
                "image": "string",
                "dob": "2022-07-26",
                "gender": "string",
                "cred": "string",
                "tags": {
                  "additionalProp1": "string",
                  "additionalProp2": "string",
                  "additionalProp3": "string"
                }
              },
              "contact": {
                "phone": "string",
                "email": "string",
                "tags": {
                  "additionalProp1": "string",
                  "additionalProp2": "string",
                  "additionalProp3": "string"
                }
              }
            },
            "agent": {
              "name": "./IFmJ>uM<$9hcxkY@.#L*'i-N1l \"mqUN.K@?F7Tb~&;V5!!L>Y7%Vo2]O9%+4s /D;lut\"G9[mY#[+Aa-+hm[[#vsioPaNPi$<[nz\\B$4X~h${[;Fa/~7.(H;\"j{:Ng$G5{l9BPt{p5ChZI:Ej1@tOL_BgASpT<Yc#~{j|L%dV=ZMc5y^wUgygQIApB:}-Odod@v5(AIO{6F:`7n/jOfKi(YL4)B~K{}`s.*p9)a 9[[D}EV!lnK#6H?:Q?0Jb';R]Q{LVcE  mv'KystEftO9SEW1ODT1-]sJN*/Mi[P/?UBA-LlD:x;F=2YP?_@Awx^X<#qNrh3K}';9;H#-[c:~o%fdJYB))^h8M<]!3dFY]^:Mh2[q):o+]5qQSEC*k:=*mP9,Y{_Uw2",
              "image": "string",
              "dob": "2022-07-26",
              "gender": "string",
              "cred": "string",
              "tags": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
              },
              "phone": "string",
              "email": "string",
              "rateable": bool
            },
            "person": {
              "name": "./4+[l_)mW%/P/MUvE-\\83H6p~\\9R~'_n']ges_\\Y+pUBb@o6}cX;IgES'uM]OxPzb;+z+5/@LRr)\"//.iS*sU3c1J`Cpi;hR_1f[=>K'8\"`jMlKe il-'8",
              "image": "string",
              "dob": "2022-07-26",
              "gender": "string",
              "cred": "string",
              "tags": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
              }
            },
            "contact": {
              "phone": "string",
              "email": "string",
              "tags": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string"
              }
            },
            "vehicle": {
              "category": "string",
              "capacity": 0,
              "make": "string",
              "model": "string",
              "size": "string",
              "variant": "string",
              "color": "string",
              "energy_type": "string",
              "registration": "string"
            },
            "start": {
              "location": {
                "id": "string",
                "descriptor": {
                  "name": "string",
                  "code": "string",
                  "symbol": "string",
                  "short_desc": "string",
                  "long_desc": "string",
                  "images": [
                    "string"
                  ],
                  "audio": "string",
                  "3d_render": "string"
                },
                "gps": "+2,              32.4746026109966",
                "address": {
                  "door": "string",
                  "name": "string",
                  "building": "string",
                  "street": "string",
                  "locality": "string",
                  "ward": "string",
                  "city": "string",
                  "state": "string",
                  "country": "string",
                  "area_code": "string"
                },
                "station_code": "string",
                "city": {
                  "name": "string",
                  "code": "string"
                },
                "country": {
                  "name": "string",
                  "code": "string"
                },
                "circle": {
                  "gps": "3,                                                          +127.6591996837954793967702866769582962811491545639941549751707289664921613073316798650931820514062821",
                  "radius": {
                    "type": "CONSTANT",
                    "value": 0,
                    "estimated_value": 0,
                    "computed_value": 0,
                    "range": {
                      "min": 0,
                      "max": 0
                    },
                    "unit": "string"
                  }
                },
                "polygon": "string",
                "3dspace": "string",
                "time": {
                  "label": "string",
                  "timestamp": "2022-07-26T11:45:19.111Z",
                  "duration": "string",
                  "range": {
                    "start": "2022-07-26T11:45:19.111Z",
                    "end": "2022-07-26T11:45:19.111Z"
                  },
                  "days": "string",
                  "schedule": {
                    "frequency": "string",
                    "holidays": [
                      "2022-07-26T11:45:19.111Z"
                    ],
                    "times": [
                      "2022-07-26T11:45:19.111Z"
                    ]
                  }
                }
              },
              "time": {
                "label": "string",
                "timestamp": "2022-07-26T11:45:19.111Z",
                "duration": "string",
                "range": {
                  "start": "2022-07-26T11:45:19.111Z",
                  "end": "2022-07-26T11:45:19.111Z"
                },
                "days": "string",
                "schedule": {
                  "frequency": "string",
                  "holidays": [
                    "2022-07-26T11:45:19.111Z"
                  ],
                  "times": [
                    "2022-07-26T11:45:19.111Z"
                  ]
                }
              },
              "instructions": {
                "name": "string",
                "code": "string",
                "symbol": "string",
                "short_desc": "string",
                "long_desc": "string",
                "images": [
                  "string"
                ],
                "audio": "string",
                "3d_render": "string"
              },
              "contact": {
                "phone": "string",
                "email": "string",
                "tags": {
                  "additionalProp1": "string",
                  "additionalProp2": "string",
                  "additionalProp3": "string"
                }
              },
              "person": {
                "name": "./I;F!VtP1e~]Jp+)*}j};PfC)&(tbL[bx+rA:)`=Nkf:/ltRS]613EluZANM;`VEn%2cR?/sx7bz8{+>i?4?#G%3Jt'<y+tEv07(oFZiYFG, mC99l]-hJ2_u#51Xp0VZ.I3*B9!h<p'_F/+>X@zwX_hl@f0 X@rq;!76TcvEfeW6H^`|0VLFU_V/[fX6^&wK]dfhq'@,s>lRh(v!Bd7 Gy(*,fB'~cK*\"9ZTt!Y2NSG)OCb~BaiBz%vo|\\F=j4`*<H,4GY@`jNf'%Bx!s+-3Mos/`S;z&f>\"y5w~W,_",
                "image": "string",
                "dob": "2022-07-26",
                "gender": "string",
                "cred": "string",
                "tags": {
                  "additionalProp1": "string",
                  "additionalProp2": "string",
                  "additionalProp3": "string"
                }
              },
              "authorization": {
                "type": "string",
                "token": "string",
                "valid_from": "2022-07-26T11:45:19.112Z",
                "valid_to": "2022-07-26T11:45:19.112Z",
                "status": "string"
              }
            },
            "end": {
              "location": {
                "id": "string",
                "descriptor": {
                  "name": "string",
                  "code": "string",
                  "symbol": "string",
                  "short_desc": "string",
                  "long_desc": "string",
                  "images": [
                    "string"
                  ],
                  "audio": "string",
                  "3d_render": "string"
                },
                "gps": "-3.614430161403440722786354071109045711811629296367248686817129609875796535178420697106357634390,                             -160.995722970843687153876299762222943621379611190825240",
                "address": {
                  "door": "string",
                  "name": "string",
                  "building": "string",
                  "street": "string",
                  "locality": "string",
                  "ward": "string",
                  "city": "string",
                  "state": "string",
                  "country": "string",
                  "area_code": "string"
                },
                "station_code": "string",
                "city": {
                  "name": "string",
                  "code": "string"
                },
                "country": {
                  "name": "string",
                  "code": "string"
                },
                "circle": {
                  "gps": "90.0000000000000000000000000,                                                         +180",
                  "radius": {
                    "type": "CONSTANT",
                    "value": 0,
                    "estimated_value": 0,
                    "computed_value": 0,
                    "range": {
                      "min": 0,
                      "max": 0
                    },
                    "unit": "string"
                  }
                },
                "polygon": "string",
                "3dspace": "string",
                "time": {
                  "label": "string",
                  "timestamp": "2022-07-26T11:45:19.113Z",
                  "duration": "string",
                  "range": {
                    "start": "2022-07-26T11:45:19.113Z",
                    "end": "2022-07-26T11:45:19.113Z"
                  },
                  "days": "string",
                  "schedule": {
                    "frequency": "string",
                    "holidays": [
                      "2022-07-26T11:45:19.113Z"
                    ],
                    "times": [
                      "2022-07-26T11:45:19.113Z"
                    ]
                  }
                }
              },
              "time": {
                "label": "string",
                "timestamp": "2022-07-26T11:45:19.113Z",
                "duration": "string",
                "range": {
                  "start": "2022-07-26T11:45:19.113Z",
                  "end": "2022-07-26T11:45:19.113Z"
                },
                "days": "string",
                "schedule": {
                  "frequency": "string",
                  "holidays": [
                    "2022-07-26T11:45:19.113Z"
                  ],
                  "times": [
                    "2022-07-26T11:45:19.113Z"
                  ]
                }
              },
              "instructions": {
                "name": "string",
                "code": "string",
                "symbol": "string",
                "short_desc": "string",
                "long_desc": "string",
                "images": [
                  "string"
                ],
                "audio": "string",
                "3d_render": "string"
              },
              "contact": {
                "phone": "string",
                "email": "string",
                "tags": {
                  "additionalProp1": "string",
                  "additionalProp2": "string",
                  "additionalProp3": "string"
                }
              },
              "person": {
                "name": "./jKv3z{n%d b(I$ (im$<#E5:.ufVj8TD&/4u$p7`8M)d-csq:78Knq`KpM +rWy,B/4^F\\jS9\\4emtV.dz9n7Z#^KBdLB'C >q\"Mam,R!3</FYF\\4^b8w*SZ*j\"&h~]7o\"Tw0UJ97g/jza-C(5_q|86fgIyj#ff@s!\"Is@v}I9Xg6ltH5l*&FDe_oL3);\"@U@[''/Vi8S#LgtAU?pIh.{oMn&p[XQ[zk\"<FO5v)Q1+\\5Id",
                "image": "string",
                "dob": "2022-07-26",
                "gender": "string",
                "cred": "string",
                "tags": {
                  "additionalProp1": "string",
                  "additionalProp2": "string",
                  "additionalProp3": "string"
                }
              },
              "authorization": {
                "type": "string",
                "token": "string",
                "valid_from": "2022-07-26T11:45:19.113Z",
                "valid_to": "2022-07-26T11:45:19.113Z",
                "status": "string"
              }
            },
            "rateable": bool,
            "tags": {
              "additionalProp1": "string",
              "additionalProp2": "string",
              "additionalProp3": "string"
            }
          }
        ],
        "payments": [
          {
            "uri": "string",
            "tl_method": "http/get",
            "params": {
              "transaction_id": "string",
              "transaction_status": "string",
              "amount": "53555381850070874850039647243744353735592737997286422987268898433298618080694065171175890556188801",
              "currency": "string",
              "additionalProp1": "string",
              "additionalProp2": "string",
              "additionalProp3": "string"
            },
            "type": "ON-ORDER",
            "status": "PAID",
            "time": {
              "label": "string",
              "timestamp": "2022-07-26T11:45:19.113Z",
              "duration": "string",
              "range": {
                "start": "2022-07-26T11:45:19.113Z",
                "end": "2022-07-26T11:45:19.113Z"
              },
              "days": "string",
              "schedule": {
                "frequency": "string",
                "holidays": [
                  "2022-07-26T11:45:19.113Z"
                ],
                "times": [
                  "2022-07-26T11:45:19.113Z"
                ]
              }
            },
            "collected_by": "BAP"
          }
        ],
        "locations": [
          {
            "id": "string",
            "descriptor": {
              "name": "string",
              "code": "string",
              "symbol": "string",
              "short_desc": "string",
              "long_desc": "string",
              "images": [
                "string"
              ],
              "audio": "string",
              "3d_render": "string"
            },
            "gps": "90,                                        109.01929195016077397400801372760989825245532358261012816863601244718233048633431871914256424",
            "address": {
              "door": "string",
              "name": "string",
              "building": "string",
              "street": "string",
              "locality": "string",
              "ward": "string",
              "city": "string",
              "state": "string",
              "country": "string",
              "area_code": "string"
            },
            "station_code": "string",
            "city": {
              "name": "string",
              "code": "string"
            },
            "country": {
              "name": "string",
              "code": "string"
            },
            "circle": {
              "gps": "90.000000000000000000000000000000000,        +96.4298354361703514468985107003804098237976575874202075286879205372050678",
              "radius": {
                "type": "CONSTANT",
                "value": 0,
                "estimated_value": 0,
                "computed_value": 0,
                "range": {
                  "min": 0,
                  "max": 0
                },
                "unit": "string"
              }
            },
            "polygon": "string",
            "3dspace": "string",
            "time": {
              "label": "string",
              "timestamp": "2022-07-26T11:45:19.114Z",
              "duration": "string",
              "range": {
                "start": "2022-07-26T11:45:19.114Z",
                "end": "2022-07-26T11:45:19.114Z"
              },
              "days": "string",
              "schedule": {
                "frequency": "string",
                "holidays": [
                  "2022-07-26T11:45:19.114Z"
                ],
                "times": [
                  "2022-07-26T11:45:19.114Z"
                ]
              }
            },
            "rateable": bool
          }
        ],
        "offers": [
          {
            "id": "string",
            "descriptor": {
              "name": "string",
              "code": "string",
              "symbol": "string",
              "short_desc": "string",
              "long_desc": "string",
              "images": [
                "string"
              ],
              "audio": "string",
              "3d_render": "string"
            },
            "location_ids": [
              "string"
            ],
            "category_ids": [
              "string"
            ],
            "item_ids": [
              "string"
            ],
            "time": {
              "label": "string",
              "timestamp": "2022-07-26T11:45:19.114Z",
              "duration": "string",
              "range": {
                "start": "2022-07-26T11:45:19.114Z",
                "end": "2022-07-26T11:45:19.114Z"
              },
              "days": "string",
              "schedule": {
                "frequency": "string",
                "holidays": [
                  "2022-07-26T11:45:19.114Z"
                ],
                "times": [
                  "2022-07-26T11:45:19.114Z"
                ]
              }
            }
          }
        ],
        "items": [
          {
            "id": "string",
            "parent_item_id": "string",
            "descriptor": {
              "name": "string",
              "code": "string",
              "symbol": "string",
              "short_desc": "string",
              "long_desc": "string",
              "images": [
                "string"
              ],
              "audio": "string",
              "3d_render": "string"
            },
            "price": {
              "currency": "string",
              "value": "514061690422425550.07808587646070067093859735901871",
              "estimated_value": "61955329861750963848872808.75865684655692247906951240359713548315334365711694057529713049774070700261675",
              "computed_value": "018581306109441.09472530016894203239552543558605870803817334925108916709790136313182913007568185798262110212119224820",
              "listed_value": "-0628717561082091338524726502690768741549317058705282975170052815608841366339294448496818514381432",
              "offered_value": "-8900704429117874882",
              "minimum_value": "+31700998424885953088.94389151384562238556415677",
              "maximum_value": "-312057078469142575842878232503398572098979198661298400881277761653988914"
            },
            "category_id": "string",
            "fulfillment_id": "string",
            "rating": 5,
            "location_id": "string",
            "time": {
              "label": "string",
              "timestamp": "2022-07-26T11:45:19.115Z",
              "duration": "string",
              "range": {
                "start": "2022-07-26T11:45:19.115Z",
                "end": "2022-07-26T11:45:19.115Z"
              },
              "days": "string",
              "schedule": {
                "frequency": "string",
                "holidays": [
                  "2022-07-26T11:45:19.115Z"
                ],
                "times": [
                  "2022-07-26T11:45:19.115Z"
                ]
              }
            },
            "rateable": bool,
            "matched": bool,
            "related": bool,
            "recommended": bool,
            "tags": {
              "additionalProp1": "string",
              "additionalProp2": "string",
              "additionalProp3": "string"
            }
          }
        ],
        "exp": "2022-07-26T11:45:19.115Z",
        "rateable": bool,
        "tags": {
          "additionalProp1": "string",
          "additionalProp2": "string",
          "additionalProp3": "string"
        }
      }








     # RESULT DATA
            data = {
                'context': context_data,
                "message": {
        "intent" : {
              "category":  category_list,
              "provider":provider_list, 
              "fulfillment": {
                "end" : {
                    "location" : {
                        "gps" : "12.4535445,77.9283792"
                    }
                }
            }
        }
    }
}
        return JsonResponse(data)
           



 