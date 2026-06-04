def recommend_solar(monthly_units):
    solar_kw = round(
        monthly_units / 120,
        1
    )
    installation_cost = (
        solar_kw * 50000
    )
    annual_savings = (
        monthly_units * 12 * 8
    )
    payback_years = round(
        installation_cost /
        annual_savings,
        1
    )
    carbon_reduction = round(
        monthly_units * 12 * 0.82 / 1000,
        2
    )
    return {
        "solar_kw": solar_kw,
        "installation_cost":
        installation_cost,
        "annual_savings":
        annual_savings,
        "payback_years":
        payback_years,
        "carbon_reduction":
        carbon_reduction
    }