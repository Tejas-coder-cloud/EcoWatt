APPLIANCES = {
    "fan": 70,        # Modern ceiling fan (Watts)
    "led": 9,         # LED bulb (Watts)
    "ac": 1400,       # 1.5 Ton inverter AC average (Watts)
    "tv": 100,        # LED TV (Watts)
    "fridge": 150     # Refrigerator average (Watts)
}
ELECTRICITY_RATE = 8  # ₹ per kWh
def calculate_energy(
    fans,
    fan_hours,
    leds,
    led_hours,
    acs,
    ac_hours,
    tvs,
    tv_hours,
    fridges
):
    fan_units = (
        fans *
        APPLIANCES["fan"] *
        fan_hours *
        30
    ) / 1000
    led_units = (
        leds *
        APPLIANCES["led"] *
        led_hours *
        30
    ) / 1000
    ac_units = (
        acs *
        APPLIANCES["ac"] *
        ac_hours *
        30
    ) / 1000
    tv_units = (
        tvs *
        APPLIANCES["tv"] *
        tv_hours *
        30
    ) / 1000
    fridge_units = (
        fridges *
        APPLIANCES["fridge"] *
        8 *
        30
    ) / 1000
    total_units = (
        fan_units +
        led_units +
        ac_units +
        tv_units +
        fridge_units
    )
    estimated_bill = (
        total_units *
        ELECTRICITY_RATE
    )
    return {
        "Fans": round(fan_units, 2),
        "LEDs": round(led_units, 2),
        "AC": round(ac_units, 2),
        "TV": round(tv_units, 2),
        "Fridge": round(fridge_units, 2),
        "Total": round(total_units, 2),
        "Bill": round(estimated_bill, 2)
    }