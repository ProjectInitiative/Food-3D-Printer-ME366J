# -----------------------------------------------------------------------------
# Hardware config.

# Maximum velocity for each axis in millimeter per minute.
MAX_VELOCITY_MM_PER_MIN_X = 900
MAX_VELOCITY_MM_PER_MIN_Y = 900
MAX_VELOCITY_MM_PER_MIN_Z = 900
MAX_VELOCITY_MM_PER_MIN_E = 900
MIN_VELOCITY_MM_PER_MIN = 1
# Average velocity for endstop calibration procedure
CALIBRATION_VELOCITY_MM_PER_MIN = 800

# Stepper motors steps per millimeter for each axis.
STEPPER_PULSES_PER_MM_X = 20*16
STEPPER_PULSES_PER_MM_Y = 20*16
STEPPER_PULSES_PER_MM_Z = 20*16
STEPPER_PULSES_PER_MM_E = 20*16

# Invert axises direction, by default(False) high level means increase of
# position. For inverted(True) axis, high level means decrease of position.
STEPPER_INVERTED_X = False
STEPPER_INVERTED_Y = False
STEPPER_INVERTED_Z = False
STEPPER_INVERTED_E = True

# Invert zero end stops switches. By default(False) low level on input pin
# means that axis in zero position. For inverted(True) end stops, high level
# means zero position.
ENDSTOP_INVERTED_X = False
ENDSTOP_INVERTED_Y = False
ENDSTOP_INVERTED_Z = False  # Auto leveler

# Workplace physical size.
TABLE_SIZE_X_MM = 270
TABLE_SIZE_Y_MM = 245
TABLE_SIZE_Z_MM = 110

# Mixed settings.
STEPPER_PULSE_LENGTH_US = 2
STEPPER_MAX_ACCELERATION_MM_PER_S2 = 3000  # for all axis, mm per sec^2
SPINDLE_MAX_RPM = 10000
EXTRUDER_MAX_TEMPERATURE = 1000
BED_MAX_TEMPERATURE = 1000
MIN_TEMPERATURE = 0
EXTRUDER_PID = {"P": 0.059161177519,
                "I": 0.00206217171374,
                "D": 0.206217171374}
BED_PID = {"P": 0.226740848076,
           "I": 0.00323956215053,
           "D": 0.323956215053}

# -----------------------------------------------------------------------------
# Pins configuration.

# Enable pin for all steppers, low level is enabled.
STEPPERS_ENABLE_PIN = 7
STEPPER_STEP_PIN_X = 25
STEPPER_STEP_PIN_Y = 23
STEPPER_STEP_PIN_Z = 15
STEPPER_STEP_PIN_E = 14

STEPPER_DIR_PIN_X = 8
STEPPER_DIR_PIN_Y = 24
STEPPER_DIR_PIN_Z = 18
STEPPER_DIR_PIN_E = 4

SPINDLE_PWM_PIN = 0
FAN_PIN = 0
EXTRUDER_HEATER_PIN = 0
BED_HEATER_PIN = 0
EXTRUDER_TEMPERATURE_SENSOR_CHANNEL = 0
BED_TEMPERATURE_SENSOR_CHANNEL = 0

ENDSTOP_PIN_X = 10
ENDSTOP_PIN_Y = 9
ENDSTOP_PIN_Z = 11

# -----------------------------------------------------------------------------
#  Behavior config

# Run command immediately after receiving and stream new pulses, otherwise
# buffer will be prepared firstly and then command will run.
# Before enabling this feature, please make sure that board performance is
# enough for streaming pulses(faster then real time).
INSTANT_RUN = False

# If this parameter is False, error will be raised on command with velocity
# more than maximum velocity specified here. If this parameter is True,
# velocity would be decreased(proportional for all axises) to fit the maximum
# velocity.
AUTO_VELOCITY_ADJUSTMENT = True

# Automatically turn on fan when extruder is heating, boolean value.
AUTO_FAN_ON = True
