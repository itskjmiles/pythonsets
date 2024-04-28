our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes & competitor_routes
print("Destinations both airlines fly to:", common_destinations)

unique_to_our_airline = our_routes - competitor_routes
print("Destinations unique to our airline:", unique_to_our_airline)

unique_to_competitor_airline = competitor_routes - our_routes
print("Destinations unique to competitor's airline:", unique_to_competitor_airline)

neither_airline_destinations = our_routes ^ competitor_routes
print("Destinations that neither airline shares:", neither_airline_destinations)
