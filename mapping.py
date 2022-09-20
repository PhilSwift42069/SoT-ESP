"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""


ships = {
    # ------------ SHIPS / AI SHIPS ------------
    "BP_SmallShipTemplate_C": {
        "Name": "Sloop (Near)",
    },
    "BP_SmallShipNetProxy_C": {
        "Name": "Sloop",
    },

    "BP_MediumShipTemplate_C": {
        "Name": "Brig (Near)",
    },
    "BP_MediumShipNetProxy_C": {
        "Name": "Brig",
    },

    "BP_LargeShipTemplate_C": {
        "Name": "Galleon (Near)",
    },
    "BP_LargeShipNetProxy_C": {
        "Name": "Galleon",
    },

    "BP_AISmallShipTemplate_C": {
        "Name": "Skeleton Sloop (Near)",
    },
    "BP_AISmallShipNetProxy_C": {
        "Name": "Skeleton Sloop",
    },
    "BP_AILargeShipTemplate_C": {
        "Name": "Skeleton Galleon (Near)",
    },
    "BP_AILargeShipNetProxy_C": {
        "Name": "Skeleton Galleon",
    },
    # "BP_AggressiveGhostShip_C": {
    #     "Name": "Flameheart Galleon",
    # },  # To implement, must modify ship.py's update method for visibility
}

test_actors = {
    
}

fishing = {
  "BP_FishingFloat_C": {
    "Super": "FishingFloat",
    "FullSize": "0x7f0",
    "InheritedSize": "0x7e0",
    "ClassSize": "0x10",
    "Attributes": [
      {
        "Name": "FishingFloatNameplate",
        "Type": "Class FishingFloatNameplateComponent*",
        "Size": "0x8",
        "Offset": "0x7e0"
      },
      {
        "Name": "StaticMesh",
        "Type": "Class StaticMeshComponent*",
        "Size": "0x8",
        "Offset": "0x7e8"
      }
    ]
  },
  "BP_FishingFish_Base_C": {
    "Super": "FishingFish",
    "FullSize": "0x920",
    "InheritedSize": "0x910",
    "ClassSize": "0x10",
    "Attributes": [
      {
        "Name": "WaterInteractionOverlap",
        "Type": "Class BoxComponent*",
        "Size": "0x8",
        "Offset": "0x910"
      },
      {
        "Name": "MaterialManipulation",
        "Type": "Class MaterialManipulationComponent*",
        "Size": "0x8",
        "Offset": "0x918"
      }
    ]
  },
  "BP_FishCreature_C": {
    "Super": "Actor",
    "FullSize": "0x4e8",
    "InheritedSize": "0x3c8",
    "ClassSize": "0x120",
    "Attributes": [
      {
        "Name": "DefaultSceneRoot",
        "Type": "Class SceneComponent*",
        "Size": "0x8",
        "Offset": "0x3c8"
      },
      {
        "Name": "CreatureType",
        "Type": "byte",
        "Size": "0x1",
        "Offset": "0x3d0"
      },
      {
        "Name": "NumOfCreatures",
        "Type": "byte",
        "Size": "0x1",
        "Offset": "0x3d1"
      },
      {
        "Name": "BoundsBias",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x3d4"
      },
      {
        "Name": "StaticMeshComponent",
        "Type": "Class StaticMeshComponent*",
        "Size": "0x8",
        "Offset": "0x3d8"
      },
      {
        "Name": "currMaterial",
        "Type": "Class MaterialInstanceDynamic*",
        "Size": "0x8",
        "Offset": "0x3e0"
      },
      {
        "Name": "MaterialInstance",
        "Type": "TArray<class MaterialInstanceDynamic*>",
        "Size": "0x10",
        "Offset": "0x3e8"
      },
      {
        "Name": "Seed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x3f8"
      },
      {
        "Name": "SwimSpeed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x3fc"
      },
      {
        "Name": "CirclingSpeed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x400"
      },
      {
        "Name": "CirclingDirection",
        "Type": "byte",
        "Size": "0x1",
        "Offset": "0x404"
      },
      {
        "Name": "CirclingRadius",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x408"
      },
      {
        "Name": "SwimDeformation",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x40c"
      },
      {
        "Name": "mud",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x410"
      },
      {
        "Name": "shoalSpeed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x414"
      },
      {
        "Name": "ShoalingSpread",
        "Type": "Struct Vector2D",
        "Size": "0x8",
        "Offset": "0x418"
      },
      {
        "Name": "ShoalingHeight",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x420"
      },
      {
        "Name": "fishSpeed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x424"
      },
      {
        "Name": "FishSpread",
        "Type": "Struct Vector2D",
        "Size": "0x8",
        "Offset": "0x428"
      },
      {
        "Name": "FishHeight",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x430"
      },
      {
        "Name": "RandomSpread",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x434"
      },
      {
        "Name": "HueVariance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x438"
      },
      {
        "Name": "Smoothness",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x43c"
      },
      {
        "Name": "SelectedCreatureType",
        "Type": "TArray<Assetclass SelectedCreatureType>",
        "Size": "0x10",
        "Offset": "0x440"
      },
      {
        "Name": "Fish_04",
        "Type": "TArray<Assetclass Fish_04>",
        "Size": "0x10",
        "Offset": "0x450"
      },
      {
        "Name": "Fish_05",
        "Type": "TArray<Assetclass Fish_05>",
        "Size": "0x10",
        "Offset": "0x460"
      },
      {
        "Name": "Size",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x470"
      },
      {
        "Name": "SizeVariance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x474"
      },
      {
        "Name": "SimSpeed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x478"
      },
      {
        "Name": "BBox",
        "Type": "Struct Vector",
        "Size": "0xc",
        "Offset": "0x47c"
      },
      {
        "Name": "Fish_07",
        "Type": "TArray<Assetclass Fish_07>",
        "Size": "0x10",
        "Offset": "0x488"
      },
      {
        "Name": "DrawDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x498"
      },
      {
        "Name": "Clown_01",
        "Type": "TArray<Assetclass Clown_01>",
        "Size": "0x10",
        "Offset": "0x4a0"
      },
      {
        "Name": "SizeCompensation",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x4b0"
      },
      {
        "Name": "Splashtail",
        "Type": "TArray<Assetclass Splashtail>",
        "Size": "0x10",
        "Offset": "0x4b8"
      },
      {
        "Name": "Pondie",
        "Type": "TArray<Assetclass Pondie>",
        "Size": "0x10",
        "Offset": "0x4c8"
      },
      {
        "Name": "FishDistribution",
        "Type": "Struct LinearColor",
        "Size": "0x10",
        "Offset": "0x4d8"
      }
    ]
  },
  "BP_PromptActor_Fishing_C": {
    "Super": "BP_PromptActorBase_C",
    "FullSize": "0x410",
    "InheritedSize": "0x400",
    "ClassSize": "0x10",
    "Attributes": [
      {
        "Name": "UberGraphFrame",
        "Type": "Struct PointerToUberGraphFrame",
        "Size": "0x8",
        "Offset": "0x400"
      },
      {
        "Name": "PromptCoordinator",
        "Type": "BlueprintGeneratedClass BP_Prompt_MaidenVoyage_FishingRodTutorial_C*",
        "Size": "0x8",
        "Offset": "0x408"
      }
    ]
  },
  "BP_gmp_fishing_rod_bdg_01_a_ItemInfo_C": {
    "Super": "ItemInfo",
    "FullSize": "0x518",
    "InheritedSize": "0x510",
    "ClassSize": "0x8",
    "Attributes": [
      {
        "Name": "DefaultSceneRoot",
        "Type": "Class SceneComponent*",
        "Size": "0x8",
        "Offset": "0x510"
      }
    ]
  }
}

ship_keys = set(ships.keys())
fishing_blueprints = set(fishing)