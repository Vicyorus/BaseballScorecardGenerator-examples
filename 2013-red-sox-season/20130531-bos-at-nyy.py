import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2013-05-31
# https://www.baseball-reference.com/boxes/NYA/NYA201305310.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2013/05/31/347555/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-31 19:08-22:01",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "45,141",
        "temp": "86F, Clear",
        "wind": "10mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                29: "Daniel Nava",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                7: "Stephen Drew",
                3: "David Ross",
                44: "Jackie Bradley Jr.",
                10: "Jose Iglesias",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                2: "Jacoby Ellsbury",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                23: "Pedro Ciriaco",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 30, 32, 22],
            "lineup": [
                [29, "7"],
                [5, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [7, "6"],
                [3, "2"],
                [44, "8"],
                [10, "5"],
            ],
            "bench": [
                [2, "CF"],
                [39, "C"],
                [37, "1B"],
                [23, "3B"],
            ],
            "bullpen": [40, 41, 56, 30, 32, 59, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 52,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                36: "Kevin Youkilis",
                24: "Robinson Canó",
                25: "Mark Teixeira",
                12: "Vernon Wells",
                17: "Jayson Nix",
                39: "David Adams",
                31: "Ichiro Suzuki",
                19: "Chris Stewart",
                # Starting pitcher
                52: "CC Sabathia",
                # Bench
                53: "Austin Romine",
                40: "Reid Brignac",
                22: "Brennan Boesch",
                33: "Travis Hafner",
                55: "Lyle Overbay",
                # Bullpen
                18: "Hiroki Kuroda",
                65: "Phil Hughes",
                27: "Shawn Kelley",
                38: "Preston Claiborne",
                48: "Boone Logan",
                41: "David Phelps",
                43: "Adam Warren",
                42: "Mariano Rivera",
                62: "Joba Chamberlain",
                30: "David Robertson",
            },
            "lefties": [52, 48],
            "lineup": [
                [11, "8"],
                [36, "0"],
                [24, "4"],
                [25, "3"],
                [12, "7"],
                [17, "6"],
                [39, "5"],
                [31, "9"],
                [19, "2"],
            ],
            "bench": [
                [53, "C"],
                [40, "SS"],
                [22, "RF"],
                [33, "DH"],
                [55, "1B"],
            ],
            "bullpen": [18, 65, 27, 38, 48, 41, 43, 42, 62, 30],
        },
        "umpires": {
            "HP": "Lance Barksdale",
            "1B": "Gary Cederstrom",
            "2B": "Vic Carapazza",
            "3B": "Chris Conroy",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: NYY #52 CC Sabathia
t1 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("c b s b f f f c")
t1.out("!K")

# 2. BOS #5  Jonny Gomes (X - X - X)
t1.new_ab()
t1.pitch_list("b b c s c")
t1.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c f f f b f")
t1.hit(2)

# 4. BOS #34 David Ortiz (X - 15 - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F7")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c b")
b1.reach("BB")
b1.thrown_out(2, "36 CS", 2, 31)

# 2. NYY #36 Kevin Youkilis (X - X - 11)
b1.new_ab()
b1.pitch_list("c c f b b b s")
b1.out("KDP2-4")

# 3. NYY #24 Robinson Canó (X - X - X)
b1.new_ab()
b1.pitch_list("b c b c")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #52 CC Sabathia
t2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c f s")
t2.out("K")

# 6. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c f")
t2.out("F7")

# 7. BOS #3  David Ross (X - X - X)
t2.new_ab()
t2.hit(2)

# 8. BOS #44 Jackie Bradley Jr. (X - 3 - X)
t2.new_ab()
t2.pitch_list("b c f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 4. NYY #25 Mark Teixeira (X - X - X)
b2.new_ab()
b2.pitch_list("b f b f b f b")
b2.reach("BB")
b2.advance(3, "12 2B")
b2.advance(4, "17 1B")

# 5. NYY #12 Vernon Wells (X - X - 25)
b2.new_ab()
b2.pitch_list("c s f b f f")
b2.hit(2)
b2.advance(3, "17 1B")
b2.advance(4, "31 1B")

# 6. NYY #17 Jayson Nix (25 - 12 - X)
b2.new_ab()
b2.pitch_list("f")
b2.hit(1, rbis=1)
b2.advance(2, "31 1B")

# 7. NYY #39 David Adams (12 - X - 17)
b2.new_ab()
b2.pitch_list("b s b d f c")
b2.out("!K")

# 8. NYY #31 Ichiro Suzuki (12 - X - 17)
b2.new_ab()
b2.pitch_list("c b f")
b2.hit(1, rbis=1)
b2.thrown_out(2, "19 DP6-4-3", 2, 31)

# 9. NYY #19 Chris Stewart (X - 17 - 31)
b2.new_ab()
b2.pitch_list("b b b c")
b2.out("DP6-4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #52 CC Sabathia
t3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.thrown_out(2, "29 DP5-4-3", 1, 52)

# 1. BOS #29 Daniel Nava (X - X - 10)
t3.new_ab()
t3.pitch_list("c b b c")
t3.out("DP5-4-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
t3.new_ab()
t3.out("F8")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b3.new_ab()
b3.pitch_list("b f b b")
b3.out("F8")

# 2. NYY #36 Kevin Youkilis (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G6-3")

# 3. NYY #24 Robinson Canó (X - X - X)
b3.new_ab()
b3.pitch_list("b c b f c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #52 CC Sabathia
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c s")
t4.out("G1-3")

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b")
t4.out("G3")

# 5. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 4. NYY #25 Mark Teixeira (X - X - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.out("G6-3")

# 5. NYY #12 Vernon Wells (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G6-3")

# 6. NYY #17 Jayson Nix (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f f b f")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #52 CC Sabathia
t5 = game.new_inning()

# 6. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("c c b b s")
t5.out("K")

# 7. BOS #3  David Ross (X - X - X)
t5.new_ab()
t5.pitch_list("s c b s")
t5.out("K")

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c s c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 7. NYY #39 David Adams (X - X - X)
b5.new_ab()
b5.pitch_list("c c")
b5.reach("HBP")
b5.thrown_out(2, "31 FC1-6", 1, 31)

# 8. NYY #31 Ichiro Suzuki (X - X - 39)
b5.new_ab()
b5.pitch_list("c b s b f")
b5.reach("FC1-6")
b5.advance(2, "19 BB")
b5.advance(4, "36 1B")

# 9. NYY #19 Chris Stewart (X - X - 31)
b5.new_ab()
b5.pitch_list("b c b b b")
b5.reach("BB")
b5.advance(2, "36 1B")
b5.thrown_out(3, "36 7-6", 3, 31)

# 1. NYY #11 Brett Gardner (X - 31 - 19)
b5.new_ab()
b5.pitch_list("f f b c")
b5.out("!K")

# 2. NYY #36 Kevin Youkilis (X - 31 - 19)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(1, rbis=1)


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #52 CC Sabathia
t6 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t6.new_ab()
t6.pitch_list("b c f")
t6.hit(1)
t6.thrown_out(2, "5 DP4-3", 2, 52)

# 1. BOS #29 Daniel Nava (X - X - 10)
t6.new_ab()
t6.pitch_list("b f f s")
t6.out("K")

# 2. BOS #5  Jonny Gomes (X - X - 10)
t6.new_ab()
t6.pitch_list("b b c b")
t6.out("DP4-3")


# Bot 6th
# Pitching: BOS #31 Jon Lester
b6 = game.new_inning()

# 3. NYY #24 Robinson Canó (X - X - X)
b6.new_ab()
b6.pitch_list("b b c b b")
b6.reach("BB")

# 4. NYY #25 Mark Teixeira (X - X - 24)
b6.new_ab()
b6.pitch_list("c b f c")
b6.out("!K")

# 5. NYY #12 Vernon Wells (X - X - 24)
b6.new_ab()
b6.out("L8")

# 6. NYY #17 Jayson Nix (X - X - 24)
b6.new_ab()
b6.pitch_list("b")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #52 CC Sabathia
t7 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(2)
t7.advance(3, "34 G3")
t7.advance(4, "12 2B")

# 4. BOS #34 David Ortiz (X - 15 - X)
t7.new_ab()
t7.pitch_list("b b s s")
t7.out("G3")

# 5. BOS #12 Mike Napoli (15 - X - X)
t7.new_ab()
t7.pitch_list("s b b")
t7.hit(2, rbis=1)

# 6. BOS #7  Stephen Drew (X - 12 - X)
t7.new_ab()
t7.pitch_list("b c f s")
t7.out("K")

# 7. BOS #3  David Ross (X - 12 - X)
t7.new_ab()
t7.pitch_list("c b c")
t7.out("G4-3")


# Bot 7th
# Pitching: BOS #31 Jon Lester
b7 = game.new_inning()

# 7. NYY #39 David Adams (X - X - X)
b7.new_ab()
b7.out("G6-3")

# 8. NYY #31 Ichiro Suzuki (X - X - X)
b7.new_ab()
b7.pitch_list("c b f")
b7.hit(1)
b7.advance(2, "19 1B")
b7.advance(4, "11 1B")

# 9. NYY #19 Chris Stewart (X - X - 31)
b7.new_ab()
b7.pitch_list("b c c")
b7.hit(1)
b7.advance(2, "11 1B")

# Pitching change (BOS): #30 Andrew Miller replaces #31 Jon Lester
b7.pitching_substitution(30)

# 1. NYY #11 Brett Gardner (X - 31 - 19)
b7.new_ab()
b7.pitch_list("c f")
b7.hit(1, rbis=1)

# 2. NYY #36 Kevin Youkilis (X - 19 - 11)
b7.new_ab()
b7.pitch_list("c c c")
b7.out("!K")

# 3. NYY #24 Robinson Canó (X - 19 - 11)
b7.new_ab()
b7.pitch_list("b c b s b c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #52 CC Sabathia
t8 = game.new_inning()

# 8. BOS #44 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("b c f")
t8.out("G3")

# Pitching change (NYY): #30 David Robertson replaces #52 CC Sabathia
t8.pitching_substitution(30)

# 9. BOS #10 Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b")
t8.out("F9")

# 1. BOS #29 Daniel Nava (X - X - X)
t8.new_ab()
t8.pitch_list("c b b c f b c")
t8.out("!K")


# Bot 8th
# Pitching: BOS #59 Clayton Mortensen
b8 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #30 Andrew Miller
b8.pitching_substitution(59)

# 4. NYY #25 Mark Teixeira (X - X - X)
b8.new_ab()
b8.pitch_list("b b c f b s")
b8.out("K")

# 5. NYY #12 Vernon Wells (X - X - X)
b8.new_ab()
b8.pitch_list("c f")
b8.out("F9")

# 6. NYY #17 Jayson Nix (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #42 Mariano Rivera
t9 = game.new_inning()

# Pitching change (NYY): #42 Mariano Rivera replaces #30 David Robertson
t9.pitching_substitution(42)

# 2. BOS #5  Jonny Gomes (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("F7")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.hit(1)
t9.advance(2, "34 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
# Offensive change (BOS): Pinch-runner #23 Pedro Ciriaco replaces #34 David Ortiz
t9.offensive_substitution(4, 23, "PR")
t9.atbase("PR")

# 5. BOS #12 Mike Napoli (X - 15 - 34)
t9.new_ab()
t9.pitch_list("c s t")
t9.out("KT")

# 6. BOS #7  Stephen Drew (X - 15 - 34)
t9.new_ab()
t9.pitch_list("c b")
t9.out("G1-3")

# Winning team: NYY
# WP: NYY #52 CC Sabathia
game.winning_pitcher(52)
# SV: NYY #42 Mariano Rivera
game.save_pitcher(42)

# Loser team: BOS
# LP: BOS #31 Jon Lester
game.losing_pitcher(31, is_away_team=True)

# print(game)
game.generate_scorecard()
