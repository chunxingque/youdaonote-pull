[


  {


    "inboundTag": [],


    "outboundTag": "proxy",


    "domain": [


      "geosite:google"


    ],


    "enabled": true


  },


  {


    "inboundTag": [],


    "outboundTag": "direct",


    "ip": [


      "geoip:cn"


    ],


    "enabled": true


  }


]










































"routing": {


  "rules": [


    {


      "type": "field",


      "outboundTag": "reject",


      "domain": ["geosite:category-ads-all"]


    },


    {


      "type": "field",


      "outboundTag": "direct",


      "ip": [


        "geoip:cn",


        "geoip:private"


      ]


    },


    {


      "type": "field",


      "outboundTag": "proxy",


      "ip": [


        "1.1.1.1/32",


        "1.0.0.1/32",


        "8.8.8.8/32",


        "8.8.4.4/32",


        "geoip:!cn"


      ]


    }


  ]


}