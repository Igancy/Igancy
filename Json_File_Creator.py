import os
from os import listdir
from os.path import isfile, join
import time

mypath = input('Enter the file path Example:"F:\Minecraft\Content\Marketing Art\ ')
dir = os.path.join(mypath + '\json\\')
if not os.path.exists(dir):
    os.mkdir(dir)

geolist = [file for file in listdir(mypath) if file.endswith('.geo.json')]
geo = []

for j in range(len(geolist)):
    x = geolist[j]
    geo.append(x.replace('.geo.json', ''))
    j+1

for i in range(len(geolist)):
    file = open(dir + geo[i] + ".json", "w")

    json = ("\n", "{", "\n",
            "  " + '"format_version"' + ": " + '"1.10.0"', ",""\n"
            , "  ", '"minecraft:client_entity"' + ": {", "\n",
            "    " + '"description"' + ": {",
            "\n" + "      " + '"identifier"' + ":" + " " + '"myth:' + geo[i] + '",', "\n",
            "      ", '"materials": {', "\n"
                                        "        " + '"default": "entity_alphatest"', "\n",
            "      " + "}," + "\n",
            "      " + '"textures"' + ": {", "\n",
            "        " + '"texture_1"' + ": " + '"textures/entity/' + geo[i] + '/1",', "\n",
            "        " + '"texture_2"' + ": " + '"textures/entity/' + geo[i] + '/2",', "\n",
            "        " + '"texture_3"' + ": " + '"textures/entity/' + geo[i] + '/3",', "\n",
            "        " + '"texture_4"' + ": " + '"textures/entity/' + geo[i] + '/4",', "\n",
            "        " + '"texture_5"' + ": " + '"textures/entity/' + geo[i] + '/5",', "\n",
            "        " + '"texture_6"' + ": " + '"textures/entity/' + geo[i] + '/6",', "\n",
            "        " + '"texture_7"' + ": " + '"textures/entity/' + geo[i] + '/7"', "\n",
            "      " + "}," + "\n",
            "        " + '"scripts"' + ": {", "\n",
            "        " + '"initialize"' + ": [", "\n",
            "		    " + '"variable.init_rot = Math.round(query.body_y_rotation / 45) * 45;"' + "," + '\n'
            "        " + '"variable.rotating = query.variant;"' + '\n',
            "      " + "]," + '\n',
            "		  " + '"animate"' + ": [" + '\n',
            "		    " + '"root"' + "," + '\n',
            "		    " + '"rotate_controller"' + '\n',
            "		  " + "]" + '\n',
            "        " + "}," + '\n',
            "      " + '"animations"' + ": {", "\n",
            "        " + '"root"' + ": " + '"controller.animation.myth.furniture.root"' + "," + "\n",
            "        " + '"spawn"' + ": " + '"animation.myth.furniture.spawn"' + "," + "\n",
            "        " + '"despawn"' + ": " + '"animation.myth.furniture.despawn"' + "," + "\n",
            "		    " + '"rotate_controller"' + ": " + '"controller.animation.myth.furniture.rotate"' + ",""\n",
            "		    " + '"rotated"' + ": " + '"animation.myth.furniture.rotated"' + ",""\n",
            "        " + '"rotating"' + ": " + '"animation.myth.furniture.rotating"' + "\n",
            "      " + "}," + '\n',
            "      " + '"render_controllers"' + ": [", "\n",
            "        " + '"controller.render.furniture.seven"' + "\n",
            "      " + "]," + '\n',
            "      " + '"spawn_egg"' + ": {", "\n",
            "        " + '"texture"' + ": " + '"' + geo[i] + '"' + "\n",
            "      " + "}," + '\n',
            "      " + '"geometry"' + ": {", "\n",
            "        " + '"default"' + ": " + '"geometry.' + geo[i] + '"' + "\n",
            "      " + "}", "\n"
                            "    " + "}", "\n"
                                          "  " + "}", "\n"
                                                      "}"
            )
    file.writelines(json)
    i+1



print("done")
