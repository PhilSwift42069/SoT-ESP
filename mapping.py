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
  "FishingFish": {
    "Super": "Character",
    "FullSize": "0x910",
    "InheritedSize": "0x5e0",
    "ClassSize": "0x330",
    "Attributes": [
      {
        "Name": "FishDataAsset",
        "Type": "Class FishDataAsset*",
        "Size": "0x8",
        "Offset": "0x5f0"
      },
      {
        "Name": "FishingMiniGameFishDataAsset",
        "Type": "Class FishingMiniGameFishDataAsset*",
        "Size": "0x8",
        "Offset": "0x5f8"
      },
      {
        "Name": "BattlingVFX",
        "Type": "Class ParticleSystemComponent*",
        "Size": "0x8",
        "Offset": "0x600"
      },
      {
        "Name": "BeingTiredVFX",
        "Type": "Class ParticleSystemComponent*",
        "Size": "0x8",
        "Offset": "0x608"
      },
      {
        "Name": "WaterInteractionComponent",
        "Type": "Class WaterInteractionComponent*",
        "Size": "0x8",
        "Offset": "0x610"
      },
      {
        "Name": "CaughtFishItemDesc",
        "Type": "class",
        "Size": "0x8",
        "Offset": "0x618"
      },
      {
        "Name": "DitherComponent",
        "Type": "Class DitherComponent*",
        "Size": "0x8",
        "Offset": "0x8b0"
      },
      {
        "Name": "MouthAttachLocation",
        "Type": "Struct Vector",
        "Size": "0xc",
        "Offset": "0x8b8"
      },
      {
        "Name": "AutoKillTime",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x8c4"
      },
      {
        "Name": "RandomAnimationLoopVal",
        "Type": "int",
        "Size": "0x4",
        "Offset": "0x8d0"
      }
    ]
  },
  "FishAnimationInstance": {
    "Super": "AnimInstance",
    "FullSize": "0x4f0",
    "InheritedSize": "0x440",
    "ClassSize": "0xb0",
    "Attributes": [
      {
        "Name": "FishSkeletalMesh",
        "Type": "Class SkeletalMesh*",
        "Size": "0x8",
        "Offset": "0x440"
      },
      {
        "Name": "FishingFishCharacter",
        "Type": "Class FishingFish*",
        "Size": "0x8",
        "Offset": "0x448"
      },
      {
        "Name": "FishingFishAnimationParams",
        "Type": "Struct FishAnimationParams",
        "Size": "0x8",
        "Offset": "0x450"
      },
      {
        "Name": "FishAnimationSequences",
        "Type": "Struct FishAnimationSequences",
        "Size": "0x88",
        "Offset": "0x458"
      },
      {
        "Name": "IsJumpActive",
        "Type": "bool",
        "Size": "0x1",
        "Offset": "0x4e0"
      },
      {
        "Name": "IsOnSurface",
        "Type": "bool",
        "Size": "0x1",
        "Offset": "0x4e1"
      },
      {
        "Name": "FishIsCaught",
        "Type": "bool",
        "Size": "0x1",
        "Offset": "0x4e2"
      },
      {
        "Name": "CurrentPlayingMontage",
        "Type": "Class AnimMontage*",
        "Size": "0x8",
        "Offset": "0x4e8"
      }
    ]
  },
  "FishDataAsset": {
    "Super": "DataAsset",
    "FullSize": "0x188",
    "InheritedSize": "0x28",
    "ClassSize": "0x160",
    "Attributes": [
      {
        "Name": "CruisingDepthBeneathWaterHeight",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x28"
      },
      {
        "Name": "RisingFromTheDepthsSpeed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x2c"
      },
      {
        "Name": "EscapingToTheDepthsSpeed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x30"
      },
      {
        "Name": "TimeReelingWhenBattlingToSnapLine",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0x38"
      },
      {
        "Name": "ReelingCooldownMultiplier",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x68"
      },
      {
        "Name": "NumberOfLoopsBeforeBiting",
        "Type": "Struct WeightedProbabilityRange",
        "Size": "0x20",
        "Offset": "0x70"
      },
      {
        "Name": "MinimumDistanceFromPlayer",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0x90"
      },
      {
        "Name": "DistanceFromPlayerToCatchFish",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xc0"
      },
      {
        "Name": "SecondsToRemainBeforeDespawning",
        "Type": "Struct FloatRange",
        "Size": "0x10",
        "Offset": "0xc4"
      },
      {
        "Name": "FloatBobDepthOnBeingHooked",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xd4"
      },
      {
        "Name": "RodBendAmountWhenBiting",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xd8"
      },
      {
        "Name": "RodBendAmountWhenBattling",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xdc"
      },
      {
        "Name": "RodBendAmountWhenRecovering",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xe0"
      },
      {
        "Name": "SplashVFXWhenBeingTired",
        "Type": "Class Object*",
        "Size": "0x8",
        "Offset": "0xe8"
      },
      {
        "Name": "SplashVFXWhenBattling",
        "Type": "Class Object*",
        "Size": "0x8",
        "Offset": "0xf0"
      },
      {
        "Name": "SplashVFXWhenJumpingOutOfWater",
        "Type": "Class Object*",
        "Size": "0x8",
        "Offset": "0xf8"
      },
      {
        "Name": "SplashVFXWhenLandingInToWater",
        "Type": "Class Object*",
        "Size": "0x8",
        "Offset": "0x100"
      },
      {
        "Name": "SplashZOffset",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x108"
      },
      {
        "Name": "FloatReelingMoveSpeedWhenMovingToMinimumDistanceFromPlayer",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x10c"
      },
      {
        "Name": "ReelingAnimationMaxSpeedWhenMovingToMinimumDistanceFromPlayer",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x110"
      },
      {
        "Name": "FloatReelingMoveSpeedWhenBattling",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x114"
      },
      {
        "Name": "ReelingAnimationMaxSpeedWhenBattling",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x118"
      },
      {
        "Name": "FloatReelingMoveSpeedWhenNotBattling",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x11c"
      },
      {
        "Name": "ReelingAnimationMaxSpeedWhenNotBattling",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x120"
      },
      {
        "Name": "TimeBetweenIsBlockedHitChecksOnServer",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x124"
      },
      {
        "Name": "TimeBeforeTurningOnHits",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x128"
      },
      {
        "Name": "HitTestTraceChannel",
        "Type": "byte",
        "Size": "0x1",
        "Offset": "0x12c"
      },
      {
        "Name": "HitDetectionHalfExtentXY",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x130"
      },
      {
        "Name": "HitDetectionHalfExtentZ",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x134"
      },
      {
        "Name": "HitDetectionZOffset",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x138"
      },
      {
        "Name": "FishingFishPool",
        "Type": "Class WwiseObjectPoolWrapper*",
        "Size": "0x8",
        "Offset": "0x140"
      },
      {
        "Name": "FishTiredSwitchGroup",
        "Type": "struct FName",
        "Size": "0x8",
        "Offset": "0x148"
      },
      {
        "Name": "FishTiredSwitchDefault",
        "Type": "struct FName",
        "Size": "0x8",
        "Offset": "0x150"
      },
      {
        "Name": "FishTiredSwitchTired",
        "Type": "struct FName",
        "Size": "0x8",
        "Offset": "0x158"
      },
      {
        "Name": "FishBiteAndStruggleStart",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x160"
      },
      {
        "Name": "FishBiteAndStruggleStop",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x168"
      },
      {
        "Name": "FishJumpOutOfWater",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x170"
      },
      {
        "Name": "FishJumpIntoWater",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x178"
      },
      {
        "Name": "FishBitingForceFeedback",
        "Type": "Class ForceFeedbackEffect*",
        "Size": "0x8",
        "Offset": "0x180"
      }
    ]
  },
  "FishingActionStateId": {
    "Super": "ActionStateId",
    "FullSize": "0x28",
    "InheritedSize": "0x28",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingConditionStatTriggerType": {
    "Super": "ConditionalStatsTriggerType",
    "FullSize": "0x30",
    "InheritedSize": "0x30",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingFloatInterface": {
    "Super": "Interface",
    "FullSize": "0x28",
    "InheritedSize": "0x28",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingRodInterface": {
    "Super": "Interface",
    "FullSize": "0x28",
    "InheritedSize": "0x28",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingFloat": {
    "Super": "Actor",
    "FullSize": "0x7e0",
    "InheritedSize": "0x3c8",
    "ClassSize": "0x418",
    "Attributes": [
      {
        "Name": "WaterInteractionComponent",
        "Type": "Class WaterInteractionComponent*",
        "Size": "0x8",
        "Offset": "0x3e0"
      },
      {
        "Name": "CollisionComponent",
        "Type": "Class BoxComponent*",
        "Size": "0x8",
        "Offset": "0x3e8"
      },
      {
        "Name": "FishingFloatSetupDataAsset",
        "Type": "Class FishingFloatSetupDataAsset*",
        "Size": "0x8",
        "Offset": "0x3f0"
      },
      {
        "Name": "FishingFloatMesh",
        "Type": "Class StaticMeshComponent*",
        "Size": "0x8",
        "Offset": "0x3f8"
      },
      {
        "Name": "FloatMaterials",
        "Type": "TArray<class MaterialInstanceDynamic*>",
        "Size": "0x10",
        "Offset": "0x400"
      }
    ]
  },
  "FishingFloatNameplateComponent": {
    "Super": "NameplateComponent",
    "FullSize": "0x390",
    "InheritedSize": "0x310",
    "ClassSize": "0x80",
    "Attributes": [
      {
        "Name": "NameplateOffset",
        "Type": "Struct Vector",
        "Size": "0xc",
        "Offset": "0x310"
      }
    ]
  },
  "FishingFloatSetupDataAsset": {
    "Super": "DataAsset",
    "FullSize": "0xc0",
    "InheritedSize": "0x28",
    "ClassSize": "0x98",
    "Attributes": [
      {
        "Name": "FishingFloatPool",
        "Type": "Class WwiseObjectPoolWrapper*",
        "Size": "0x8",
        "Offset": "0x28"
      },
      {
        "Name": "RodCastFloatLandInWater",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x30"
      },
      {
        "Name": "DelayBeforeDetachingFloat",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x38"
      },
      {
        "Name": "FloatBobDepthWhenMovedAndNotHooked",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x3c"
      },
      {
        "Name": "RetractingDuration",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x40"
      },
      {
        "Name": "ViolentlyRetractingDuration",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x44"
      },
      {
        "Name": "CastingFloatMovementXY",
        "Type": "Class CurveFloat*",
        "Size": "0x8",
        "Offset": "0x48"
      },
      {
        "Name": "CastingFloatMovementZAtMinDistance",
        "Type": "Class CurveFloat*",
        "Size": "0x8",
        "Offset": "0x50"
      },
      {
        "Name": "CastingFloatMovementZAtMaxDistance",
        "Type": "Class CurveFloat*",
        "Size": "0x8",
        "Offset": "0x58"
      },
      {
        "Name": "ReelingInFloatMovementXY",
        "Type": "Class CurveFloat*",
        "Size": "0x8",
        "Offset": "0x60"
      },
      {
        "Name": "ReelingInFloatMovementZ",
        "Type": "Class CurveFloat*",
        "Size": "0x8",
        "Offset": "0x68"
      },
      {
        "Name": "SplashVFXWhenFloatLandsOnWater",
        "Type": "Class Object*",
        "Size": "0x8",
        "Offset": "0x70"
      },
      {
        "Name": "MaxAboveDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x78"
      },
      {
        "Name": "MaxBelowDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x7c"
      },
      {
        "Name": "ExtraOffsetWhenFishNotAttached",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x80"
      },
      {
        "Name": "MaxDriftCompensationOffset",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x84"
      },
      {
        "Name": "FloatBobDepthOnComedyItemBeingHooked",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x88"
      },
      {
        "Name": "BringingInCatchDuration",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x8c"
      },
      {
        "Name": "FloatZOffset",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x90"
      },
      {
        "Name": "WobbleSpeed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x94"
      },
      {
        "Name": "MinWobbleAngle",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x98"
      },
      {
        "Name": "MaxWobbleAngle",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x9c"
      },
      {
        "Name": "TimeToBlendAwaySway",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xa0"
      },
      {
        "Name": "WobbleYawAngleOffset",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xa4"
      },
      {
        "Name": "FlavourYawMinTimeToNextChange",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xa8"
      },
      {
        "Name": "FlavourYawMaxTimeToNextChange",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xac"
      },
      {
        "Name": "FlavourYawMinSpeed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xb0"
      },
      {
        "Name": "FlavourYawMaxSpeed",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xb4"
      },
      {
        "Name": "FlavourYawAcceleration",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xb8"
      }
    ]
  },
  "FishingFreeLookConstrainsDataAsset": {
    "Super": "DataAsset",
    "FullSize": "0x40",
    "InheritedSize": "0x28",
    "ClassSize": "0x18",
    "Attributes": [
      {
        "Name": "YawDegrees",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x28"
      },
      {
        "Name": "PitchMinDegrees",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x2c"
      },
      {
        "Name": "PitchMaxDegrees",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x30"
      },
      {
        "Name": "LookAroundRightStickInputToAngleModifier",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x34"
      },
      {
        "Name": "LookAroundMouseInputToAngleModifier",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x38"
      },
      {
        "Name": "LookAroundMouseInputAsMovementInputModifier",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x3c"
      }
    ]
  },
  "FishingInputComponent": {
    "Super": "AthenaCharacterBaseInputComponent",
    "FullSize": "0x2e0",
    "InheritedSize": "0x298",
    "ClassSize": "0x48",
    "Attributes": []
  },
  "FishingLineRenderComponent": {
    "Super": "RopeCatenaryRenderComponent",
    "FullSize": "0x670",
    "InheritedSize": "0x660",
    "ClassSize": "0x10",
    "Attributes": [
      {
        "Name": "LineColour",
        "Type": "Struct LinearColor",
        "Size": "0x10",
        "Offset": "0x660"
      }
    ]
  },
  "FishingMiniGameFishDataAsset": {
    "Super": "DataAsset",
    "FullSize": "0x130",
    "InheritedSize": "0x28",
    "ClassSize": "0x108",
    "Attributes": [
      {
        "Name": "ChanceOfEscapePositionBeingLeft",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x28"
      },
      {
        "Name": "ChanceOfEscapePositionBeingAway",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x2c"
      },
      {
        "Name": "ChanceOfEscapePositionBeingRight",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x30"
      },
      {
        "Name": "HowLongBeforeUnfoughtFishEscapes",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0x38"
      },
      {
        "Name": "TimeToTire",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0x68"
      },
      {
        "Name": "SwitchesBeforeRecovery",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0x98"
      },
      {
        "Name": "TimeSpentRecovering",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0xc8"
      },
      {
        "Name": "SpeedMovingBackToCentreWhenRecovering",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xf8"
      },
      {
        "Name": "SpeedMovingBackToCentreWhenRecoveringWhenReeling",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xfc"
      },
      {
        "Name": "NumFakeOuts",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0x100"
      }
    ]
  },
  "FishingMiniGameSetupDataAsset": {
    "Super": "DataAsset",
    "FullSize": "0xa8",
    "InheritedSize": "0x28",
    "ClassSize": "0x80",
    "Attributes": [
      {
        "Name": "EscapeRadiusAtMaxDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x28"
      },
      {
        "Name": "EscapeRadiusAtMinDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x2c"
      },
      {
        "Name": "PercentageOfEscapeRadiusToKeepFishFacingOutwards",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x30"
      },
      {
        "Name": "AwayEscapeSectorAngleAtMaxDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x34"
      },
      {
        "Name": "AwayEscapeSectorAngleAtMinDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x38"
      },
      {
        "Name": "LeftRightEscapeSectorAngleAtMaxDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x3c"
      },
      {
        "Name": "LeftRightEscapeSectorAngleAtMinDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x40"
      },
      {
        "Name": "TimeToNextAngleChangeWithinSector",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0x48"
      },
      {
        "Name": "FakeOutDistancePercentage",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0x78"
      }
    ]
  },
  "FishingMouseXAnalogInputId": {
    "Super": "AnalogInputId",
    "FullSize": "0x38",
    "InheritedSize": "0x38",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingMouseYAnalogInputId": {
    "Super": "AnalogInputId",
    "FullSize": "0x38",
    "InheritedSize": "0x38",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingMoveRightInputId": {
    "Super": "AnalogInputId",
    "FullSize": "0x38",
    "InheritedSize": "0x38",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingMoveForwardInputId": {
    "Super": "AnalogInputId",
    "FullSize": "0x38",
    "InheritedSize": "0x38",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingRightStickXAnalogInputId": {
    "Super": "AnalogInputId",
    "FullSize": "0x38",
    "InheritedSize": "0x38",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingRightStickYAnalogInputId": {
    "Super": "AnalogInputId",
    "FullSize": "0x38",
    "InheritedSize": "0x38",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingRodActionStateInterface": {
    "Super": "Interface",
    "FullSize": "0x28",
    "InheritedSize": "0x28",
    "ClassSize": "0x0",
    "Attributes": []
  },
  "FishingRod": {
    "Super": "SkeletalMeshWieldableItem",
    "FullSize": "0xb90",
    "InheritedSize": "0x780",
    "ClassSize": "0x410",
    "Attributes": [
      {
        "Name": "AuxiliaryRadialCategoryFilter",
        "Type": "class",
        "Size": "0x8",
        "Offset": "0x7a0"
      },
      {
        "Name": "AuxiliaryRadialAllowedItems",
        "Type": "TArray<Class AuxiliaryRadialAllowedItems>",
        "Size": "0x10",
        "Offset": "0x7a8"
      },
      {
        "Name": "InventoryItem",
        "Type": "Class InventoryItemComponent*",
        "Size": "0x8",
        "Offset": "0x7b8"
      },
      {
        "Name": "FishSelector",
        "Type": "Struct FishingFishSelector",
        "Size": "0xd8",
        "Offset": "0x7c0"
      },
      {
        "Name": "FishingRodSetupDataAsset",
        "Type": "Class FishingRodSetupDataAsset*",
        "Size": "0x8",
        "Offset": "0x898"
      },
      {
        "Name": "FishingSetupDataAssetInToSea",
        "Type": "Class FishingSetupDataAsset*",
        "Size": "0x8",
        "Offset": "0x8a0"
      },
      {
        "Name": "FishingSetupDataAssetInToPond",
        "Type": "Class FishingSetupDataAsset*",
        "Size": "0x8",
        "Offset": "0x8a8"
      },
      {
        "Name": "FishingMiniGameSetupDataAssetInToSea",
        "Type": "Class FishingMiniGameSetupDataAsset*",
        "Size": "0x8",
        "Offset": "0x8b0"
      },
      {
        "Name": "FishingMiniGameSetupDataAssetInToPond",
        "Type": "Class FishingMiniGameSetupDataAsset*",
        "Size": "0x8",
        "Offset": "0x8b8"
      },
      {
        "Name": "FishingFreeLookConstrainsDataAsset",
        "Type": "Class FishingFreeLookConstrainsDataAsset*",
        "Size": "0x8",
        "Offset": "0x8c0"
      },
      {
        "Name": "MaterialManipulationComponent",
        "Type": "Class MaterialManipulationComponent*",
        "Size": "0x8",
        "Offset": "0x8c8"
      },
      {
        "Name": "Rope",
        "Type": "Class FishingLineRenderComponent*",
        "Size": "0x8",
        "Offset": "0x8d0"
      },
      {
        "Name": "InteractionPointOffset",
        "Type": "Struct Vector",
        "Size": "0xc",
        "Offset": "0x8d8"
      },
      {
        "Name": "StatTriggerForCatchingAFish",
        "Type": "class",
        "Size": "0x8",
        "Offset": "0x8e8"
      },
      {
        "Name": "ServerState",
        "Type": "byte",
        "Size": "0x1",
        "Offset": "0x8f0"
      },
      {
        "Name": "IsReeling",
        "Type": "bool",
        "Size": "0x1",
        "Offset": "0x8f1"
      },
      {
        "Name": "ReplicatedFishState",
        "Type": "Struct FishingRodReplicatedFishState",
        "Size": "0x10",
        "Offset": "0x8f8"
      },
      {
        "Name": "FishInteractionProxy",
        "Type": "Class Actor*",
        "Size": "0x8",
        "Offset": "0x908"
      },
      {
        "Name": "FishingMiniGamePlayerInput",
        "Type": "Struct FishingMiniGamePlayerInput",
        "Size": "0x3",
        "Offset": "0x910"
      },
      {
        "Name": "PlayerIsBattlingFish",
        "Type": "bool",
        "Size": "0x1",
        "Offset": "0x913"
      },
      {
        "Name": "BaitOnFloat",
        "Type": "Class ItemProxy*",
        "Size": "0x8",
        "Offset": "0x918"
      },
      {
        "Name": "FishingFloatRelativeCentreLocation",
        "Type": "Struct Vector",
        "Size": "0xc",
        "Offset": "0x920"
      },
      {
        "Name": "FishingFloatOffset",
        "Type": "Struct Vector",
        "Size": "0xc",
        "Offset": "0x92c"
      },
      {
        "Name": "CastIsInToAPond",
        "Type": "bool",
        "Size": "0x1",
        "Offset": "0x938"
      },
      {
        "Name": "CaughtFishClass",
        "Type": "class",
        "Size": "0x8",
        "Offset": "0x940"
      },
      {
        "Name": "BaitOnRodType",
        "Type": "byte",
        "Size": "0x1",
        "Offset": "0x948"
      },
      {
        "Name": "BattlingState",
        "Type": "byte",
        "Size": "0x1",
        "Offset": "0x949"
      },
      {
        "Name": "ComedyItemOnFloat",
        "Type": "Class ItemProxy*",
        "Size": "0x8",
        "Offset": "0x950"
      },
      {
        "Name": "CaughtComedyItemDesc",
        "Type": "class",
        "Size": "0x8",
        "Offset": "0x958"
      },
      {
        "Name": "TimeReelingWhenBattlingBeforeSnapping",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x960"
      },
      {
        "Name": "FishingMiniGamePercentageInToEscaping",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x964"
      },
      {
        "Name": "MinimumDistanceFromPlayer",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x968"
      },
      {
        "Name": "FishingFloatActor",
        "Type": "Class Actor*",
        "Size": "0x8",
        "Offset": "0x970"
      },
      {
        "Name": "LocalOnlyBaitOnFloat",
        "Type": "Class ItemProxy*",
        "Size": "0x8",
        "Offset": "0x978"
      },
      {
        "Name": "FishingMiniGame",
        "Type": "Struct FishingMiniGame",
        "Size": "0x50",
        "Offset": "0x980"
      },
      {
        "Name": "NonReplicatedLocalFishingFishOnRod",
        "Type": "Class FishingFish*",
        "Size": "0x8",
        "Offset": "0x9d0"
      },
      {
        "Name": "LocalOnlyComedyItemOnFloat",
        "Type": "Class ItemProxy*",
        "Size": "0x8",
        "Offset": "0x9d8"
      },
      {
        "Name": "IsInFishingActionState",
        "Type": "bool",
        "Size": "0x1",
        "Offset": "0x9e0"
      }
    ]
  },
  "FishingRodSetupDataAsset": {
    "Super": "DataAsset",
    "FullSize": "0x1a0",
    "InheritedSize": "0x28",
    "ClassSize": "0x178",
    "Attributes": [
      {
        "Name": "FishActorInteractionDesc",
        "Type": "class",
        "Size": "0x8",
        "Offset": "0x28"
      },
      {
        "Name": "DelayBeforeAllowingACast",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x30"
      },
      {
        "Name": "DelayBeforeCreatingFishingFloat",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x34"
      },
      {
        "Name": "DelayBeforeDestroyingFishingFloat",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x38"
      },
      {
        "Name": "FishingFloatType",
        "Type": "class",
        "Size": "0x8",
        "Offset": "0x40"
      },
      {
        "Name": "HitTestTraceChannel",
        "Type": "byte",
        "Size": "0x1",
        "Offset": "0x48"
      },
      {
        "Name": "PreCastingPlayerSpeedModifier",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x4c"
      },
      {
        "Name": "CastingTimeBeforeTurningOnHits",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x50"
      },
      {
        "Name": "TimeBetweenIsFloatLocationValidChecks",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x54"
      },
      {
        "Name": "SingleFishAnimationLoopDuration",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x58"
      },
      {
        "Name": "DriftOffsetToStopFishJumping",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x5c"
      },
      {
        "Name": "FishBreeds",
        "Type": "TArray<Struct DebugFishSelectionBreed>",
        "Size": "0x10",
        "Offset": "0x60"
      },
      {
        "Name": "FishBreedsInAPond",
        "Type": "TArray<Struct DebugFishSelectionBreed>",
        "Size": "0x10",
        "Offset": "0x70"
      },
      {
        "Name": "ForceFeedbackLevels",
        "Type": "TArray<Struct FishingRodForceFeedbackLevel>",
        "Size": "0x10",
        "Offset": "0x80"
      },
      {
        "Name": "ComedyItems",
        "Type": "TArray<Struct FishingComedyItemInfo>",
        "Size": "0x10",
        "Offset": "0x90"
      },
      {
        "Name": "ChanceOfComedyItems",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xa0"
      },
      {
        "Name": "DistanceFromPlayerToCatchComedyItem",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xa4"
      },
      {
        "Name": "FishBait",
        "Type": "TArray<Struct FishBaitInfo>",
        "Size": "0x10",
        "Offset": "0xa8"
      },
      {
        "Name": "RopeThickness",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xb8"
      },
      {
        "Name": "RopeSlackAtMaxDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xbc"
      },
      {
        "Name": "RopeSlackAtMinDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xc0"
      },
      {
        "Name": "RopeOnRodSlack",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xc4"
      },
      {
        "Name": "RopeOnRodMaxSway",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xc8"
      },
      {
        "Name": "TimeToBlendAwaySway",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xcc"
      },
      {
        "Name": "MaxTimeToWaitForAnimationStateToFinish",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xd0"
      },
      {
        "Name": "ServerEstimateRodEndPosition",
        "Type": "Struct Vector",
        "Size": "0xc",
        "Offset": "0xd4"
      },
      {
        "Name": "ServerEstimateRodBasePosition",
        "Type": "Struct Vector",
        "Size": "0xc",
        "Offset": "0xe0"
      },
      {
        "Name": "RodBaseHitDetectionExtraOffset",
        "Type": "Struct Vector",
        "Size": "0xc",
        "Offset": "0xec"
      },
      {
        "Name": "MinimumShakeValue",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xf8"
      },
      {
        "Name": "ReelingCooldownMultiplier",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xfc"
      },
      {
        "Name": "RodCastAudioDrawBack",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x100"
      },
      {
        "Name": "RodCastAudioCast",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x108"
      },
      {
        "Name": "RodBendStart",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x110"
      },
      {
        "Name": "RodBendStop",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x118"
      },
      {
        "Name": "RodBendFactorAmountToTriggerSound",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x120"
      },
      {
        "Name": "AmountOfWrongDirectionStrainToTriggerSound",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x124"
      },
      {
        "Name": "RodBendCooldown",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x128"
      },
      {
        "Name": "RodBendFactorRtpc",
        "Type": "struct FName",
        "Size": "0x8",
        "Offset": "0x12c"
      },
      {
        "Name": "RodCastReelLoopStart",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x138"
      },
      {
        "Name": "RodCastReelLoopStop",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x140"
      },
      {
        "Name": "RodCastReelSpeedRtpc",
        "Type": "struct FName",
        "Size": "0x8",
        "Offset": "0x148"
      },
      {
        "Name": "RtpcSpeedFactorCasting",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x150"
      },
      {
        "Name": "RtpcSpeedFactorFishing",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x154"
      },
      {
        "Name": "RtpcSpeedFactorReeling",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x158"
      },
      {
        "Name": "FishingBendWrongDirectionStart",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x160"
      },
      {
        "Name": "FishingBendWrongDirectionStop",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x168"
      },
      {
        "Name": "FishingLineSnap",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x170"
      },
      {
        "Name": "RodCastFishOutOfWaterWriggling",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x178"
      },
      {
        "Name": "FishingRodPool",
        "Type": "Class WwiseObjectPoolWrapper*",
        "Size": "0x8",
        "Offset": "0x180"
      },
      {
        "Name": "RodStrainMagnitudeRtpc",
        "Type": "struct FName",
        "Size": "0x8",
        "Offset": "0x188"
      },
      {
        "Name": "FishTakenFromRod",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x190"
      },
      {
        "Name": "BaitAddedToHook",
        "Type": "Class WwiseEvent*",
        "Size": "0x8",
        "Offset": "0x198"
      }
    ]
  },
  "FishingSetupDataAsset": {
    "Super": "DataAsset",
    "FullSize": "0x118",
    "InheritedSize": "0x28",
    "ClassSize": "0xf0",
    "Attributes": [
      {
        "Name": "CastDistanceMin",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x28"
      },
      {
        "Name": "CastDistanceMax",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x2c"
      },
      {
        "Name": "PreCastTimeForMaxCastDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x30"
      },
      {
        "Name": "DistanceRequiredToReelInToCatchTheFish",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x34"
      },
      {
        "Name": "MinFloatDistanceFromPlayer",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x38"
      },
      {
        "Name": "MaxFishSpawnDepth",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x3c"
      },
      {
        "Name": "CastingThrowDurationAtMinDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x40"
      },
      {
        "Name": "CastingThrowDurationAtMaxDistance",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x44"
      },
      {
        "Name": "FishSpawnHitDetectionHalfExtentXY",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x48"
      },
      {
        "Name": "FishSpawnHitDetectionHalfExtentZ",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x4c"
      },
      {
        "Name": "TimeBeforeAppearing",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0x50"
      },
      {
        "Name": "DelayBeforeTrackingFloat",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x80"
      },
      {
        "Name": "MaxDistanceFromFloatBeforeFishGivesUp",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x84"
      },
      {
        "Name": "TimeSpentBiting",
        "Type": "Struct WeightedProbabilityRangeOfRanges",
        "Size": "0x30",
        "Offset": "0x88"
      },
      {
        "Name": "FloatReelingMoveSpeedWhenNoFishOnLine",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xb8"
      },
      {
        "Name": "ReelingAnimationMaxSpeedWhenNoFishOnLine",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xbc"
      },
      {
        "Name": "ReelingAnimationSpeedChangePerSec",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xc0"
      },
      {
        "Name": "ReelingAnimationStoppingSpeedChangePerSec",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xc4"
      },
      {
        "Name": "MaxReelingWhenFailedTime",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xc8"
      },
      {
        "Name": "FishingMiniGameLeftRightInputAngle",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xcc"
      },
      {
        "Name": "FishingMiniGameBattlingAngle",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xd0"
      },
      {
        "Name": "FishingMiniGameInputThreshold",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xd4"
      },
      {
        "Name": "TimeBeforeTurningOnFishHits",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xd8"
      },
      {
        "Name": "FOVChangeWhenBattling",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xdc"
      },
      {
        "Name": "FOVBlendSpeedWhenBattling",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xe0"
      },
      {
        "Name": "TimeBeforeDestroyingFishAndAwardingPlayer",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xe4"
      },
      {
        "Name": "CameraYawFishMaxOffset",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xe8"
      },
      {
        "Name": "CameraMaxYaw",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xec"
      },
      {
        "Name": "CameraYawSpringAcc",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xf0"
      },
      {
        "Name": "CameraYawSpringAccWhenResetting",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xf4"
      },
      {
        "Name": "CameraExtraPitchWhenPullingBack",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xf8"
      },
      {
        "Name": "CameraExtraPitchSpringAcc",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0xfc"
      },
      {
        "Name": "CameraExtraPitchSpringAccWhenResetting",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x100"
      },
      {
        "Name": "BlendBackFromDisabledCameraDuration",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x104"
      },
      {
        "Name": "RodDirectionBendMaxAngleOfFishFromFromRod",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x108"
      },
      {
        "Name": "RodDirectionMaxBendLeft",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x10c"
      },
      {
        "Name": "RodDirectionMaxBendRight",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x110"
      },
      {
        "Name": "ReturnFromFreeLookSpringAcc",
        "Type": "float",
        "Size": "0x4",
        "Offset": "0x114"
      }
    ]
  },
  "FishItemConditionalStatTrigger": {
    "Super": "ConditionalStatsTriggerType",
    "FullSize": "0x30",
    "InheritedSize": "0x30",
    "ClassSize": "0x0",
    "Attributes": []
  },
}

ship_keys = set(ships.keys())
#fishing_actors = set(fishing.keys())