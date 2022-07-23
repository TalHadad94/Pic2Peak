import bpy
import csv
from math import radians

class Pic2Peak(bpy.types.Operator):
    bl_idname = "object.my_operator"
    bl_label = "Pic2Peak"

    def execute(self, context):
        
        def BuildObject (x,y,z=0): # Bulid cube in the x,y place:
            z = y * 100
            if(objectName == 'Tree'):
                bpy.ops.mesh.primitive_cone_add(enter_editmode=False, align='WORLD',
                                                location=(x*64/5, y*48/5, z), scale=(1, 1, 1))
            else:
                bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD',
                                                location=(x*64/5, y*48/5, z), scale=(1, 1, 1))  
            bpy.context.active_object.rotation_euler[0] += radians(270)                      
            bpy.context.object.name = objectName
        
        data = []
        with open("D:\Downloads\DataTable.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                # Extract the location (X,Y) of the object
                tmp = row[2].split(",")
                xtmp = tmp[0].replace("[","")
                x = float(xtmp)
                ytmp = tmp[1].replace("]","") 
                y = float(ytmp)
                # Extract the name of the Object
                objectName = row[0].replace("'","").replace("b","",1)
                # Extarct the Chance of that object to be in the Enviroment
                detectedChance = float(row[1])*100
                
                objlist = []
                objlist.append(objectName)
                objlist.append(detectedChance)
                objlist.append(x)
                objlist.append(y)
                data.append(objlist)
                print(objlist)
                
                if detectedChance > 10:
                    BuildObject(x,y)
        
        return {'FINISHED'}


def register():
    bpy.utils.register_class(Pic2Peak)


def unregister():
    bpy.utils.unregister_class(Pic2Peak)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.my_operator()