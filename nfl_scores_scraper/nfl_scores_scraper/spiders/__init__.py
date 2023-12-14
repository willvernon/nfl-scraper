import scrapy


class NFLScores(scrapy.Spider):
    name = "nfl_scores"
    start_urls = [
        #  "https://www.pro-football-reference.com/years/2023/week_1.htm",
        # "https://www.pro-football-reference.com/years/2023/week_2.htm",
        #  "https://www.pro-football-reference.com/years/2023/week_3.htm",
        # "https://www.pro-football-reference.com/years/2023/week_4.htm",
        # "https://www.pro-football-reference.com/years/2023/week_5.htm",
        # "https://www.pro-football-reference.com/years/2023/week_6.htm",
        # "https://www.pro-football-reference.com/years/2023/week_7.htm",
        # "https://www.pro-football-reference.com/years/2023/week_8.htm",
        # "https://www.pro-football-reference.com/years/2023/week_9.htm",
        # "https://www.pro-football-reference.com/years/2023/week_10.htm",
        # "https://www.pro-football-reference.com/years/2023/week_11.htm",
        # "https://www.pro-football-reference.com/years/2023/week_12.htm",
        # "https://www.pro-football-reference.com/years/2023/week_13.htm",
        "https://www.pro-football-reference.com/years/2023/week_14.htm",
        # "https://www.pro-football-reference.com/years/2023/week_15.htm",
        # "https://www.pro-football-reference.com/years/2023/week_16.htm",
        # "https://www.pro-football-reference.com/years/2023/week_17.htm",
        # "https://www.pro-football-reference.com/years/2023/week_18.htm",
    ]
    custom_settings = {
        "FEED_EXPORT_FIELDS": [
            "date",
            "week",
            "winning_team",
            "winning_team_score",
            "losing_team",
            "losing_team_score",
        ],
    }

    def parse(self, response):
        game = 1
        week = (
            response.url.split("/")[-1].split("_")[-1].split(".")[0]
        )  # Extract week from URL
        while game <= 16:
            date = response.css(
                f"#content > div.game_summaries > div:nth-child({game}) > table.teams > tbody > tr.date > td::text"
            ).extract_first()
            winning_team = response.css(
                f"#content > div.game_summaries > div:nth-child({game}) > table.teams > tbody > tr.winner > td:nth-child(1) > a::text"
            ).extract_first()
            winning_team_score = response.css(
                f"#content > div.game_summaries > div:nth-child({game}) > table.teams > tbody > tr.winner > td:nth-child(2)::text"
            ).extract_first()
            losing_team = response.css(
                f"#content > div.game_summaries > div:nth-child({game}) > table.teams > tbody > tr.loser > td:nth-child(1) > a::text"
            ).extract_first()
            losing_team_score = response.css(
                f"#content > div.game_summaries > div:nth-child({game}) > table.teams > tbody > tr.loser > td:nth-child(2)::text"
            ).extract_first()
            yield {
                "date": date,
                "week": week,
                "winning_team": winning_team,
                "winning_team_score": winning_team_score,
                "losing_team": losing_team,
                "losing_team_score": losing_team_score,
            }
            game += 1


# ------------------------------------------------------------------------------------------
# Data

# Date
# content > div.game_summaries > div:nth-child(1) > table.teams > tbody > tr.date > td
# content > div.game_summaries > div:nth-child(6) > table.teams > tbody > tr.date > td

# Winner
# content > div.game_summaries > div:nth-child(1) > table.teams > tbody > tr.winner > td:nth-child(1) > a
# content > div.game_summaries > div:nth-child(2) > table.teams > tbody > tr.winner > td:nth-child(1) > a
# content > div.game_summaries > div:nth-child(3) > table.teams > tbody > tr.winner > td:nth-child(1) > a
# content > div.game_summaries > div:nth-child(4) > table.teams > tbody > tr.winner > td:nth-child(1) > a
# content > div.game_summaries > div:nth-child(5) > table.teams > tbody > tr.winner > td:nth-child(1) > a

# Winner Score
# content > div.game_summaries > div:nth-child(1) > table.teams > tbody > tr.winner > td:nth-child(2)
# content > div.game_summaries > div:nth-child(2) > table.teams > tbody > tr.winner > td:nth-child(2)
# content > div.game_summaries > div:nth-child(3) > table.teams > tbody > tr.winner > td:nth-child(2)
# content > div.game_summaries > div:nth-child(4) > table.teams > tbody > tr.winner > td:nth-child(2)
# content > div.game_summaries > div:nth-child(5) > table.teams > tbody > tr.winner > td:nth-child(2)

# ------------------------------------------------------------------------------------------------------------

# Loser
# content > div.game_summaries > div:nth-child(1) > table.teams > tbody > tr.loser > td:nth-child(1) > a
# content > div.game_summaries > div:nth-child(2) > table.teams > tbody > tr.loser > td:nth-child(1) > a
# content > div.game_summaries > div:nth-child(3) > table.teams > tbody > tr.loser > td:nth-child(1) > a
# content > div.game_summaries > div:nth-child(4) > table.teams > tbody > tr.loser > td:nth-child(1) > a
# content > div.game_summaries > div:nth-child(5) > table.teams > tbody > tr.loser > td:nth-child(1) > a

# Loser Score
# content > div.game_summaries > div:nth-child(1) > table.teams > tbody > tr.loser > td:nth-child(2)
# content > div.game_summaries > div:nth-child(2) > table.teams > tbody > tr.loser > td:nth-child(2)
# content > div.game_summaries > div:nth-child(3) > table.teams > tbody > tr.loser > td:nth-child(2)
# content > div.game_summaries > div:nth-child(4) > table.teams > tbody > tr.loser > td:nth-child(2)
# content > div.game_summaries > div:nth-child(5) > table.teams > tbody > tr.loser > td:nth-child(2)
