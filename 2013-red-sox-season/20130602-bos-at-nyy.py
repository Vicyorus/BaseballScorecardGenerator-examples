import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2013-06-02
# https://www.baseball-reference.com/boxes/NYA/NYA201306020.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2013/06/02/347585/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-02 20:50-00:55 +1 (2:07 delay)",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "43,613",
        "temp": "81F, Cloudy",
        "wind": "10mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                29: "Daniel Nava",
                37: "Mike Carp",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                10: "Jose Iglesias",
                44: "Jackie Bradley Jr.",
                # Starting pitcher
                11: "Clay Buchholz",
                # Bench
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [29, "7"],
                [37, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [7, "6"],
                [39, "2"],
                [10, "5"],
                [44, "8"],
            ],
            "bench": [
                [2, "CF"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [40, 41, 56, 30, 32, 31, 59, 36, 19, 22, 46],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 18,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                24: "Robinson Canó",
                25: "Mark Teixeira",
                33: "Travis Hafner",
                12: "Vernon Wells",
                36: "Kevin Youkilis",
                31: "Ichiro Suzuki",
                17: "Jayson Nix",
                53: "Austin Romine",
                # Starting pitcher
                18: "Hiroki Kuroda",
                # Bench
                19: "Chris Stewart",
                40: "Reid Brignac",
                22: "Brennan Boesch",
                55: "Lyle Overbay",
                39: "David Adams",
                # Bullpen
                65: "Phil Hughes",
                27: "Shawn Kelley",
                52: "CC Sabathia",
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
                [24, "4"],
                [25, "3"],
                [33, "0"],
                [12, "7"],
                [36, "5"],
                [31, "9"],
                [17, "6"],
                [53, "2"],
            ],
            "bench": [
                [19, "C"],
                [40, "SS"],
                [22, "RF"],
                [55, "1B"],
                [39, "3B"],
            ],
            "bullpen": [65, 27, 52, 38, 48, 41, 43, 42, 62, 30],
        },
        "umpires": {
            "HP": "Vic Carapazza",
            "1B": "Chris Conroy",
            "2B": "Lance Barksdale",
            "3B": "Gary Cederstrom",
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
# Pitching: NYY #18 Hiroki Kuroda
t1 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("c c f b")
t1.out("G3")

# 2. BOS #37 Mike Carp (X - X - X)
t1.new_ab()
t1.pitch_list("c b f b c")
t1.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("F8")


# Bot 1st
# Pitching: BOS #11 Clay Buchholz
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c c f")
b1.out("G3")

# 2. NYY #24 Robinson Canó (X - X - X)
b1.new_ab()
b1.pitch_list("b b f c b b")
b1.reach("BB")

# 3. NYY #25 Mark Teixeira (X - X - 24)
b1.new_ab()
b1.pitch_list("b 1 t f b c")
b1.out("!K")

# 4. NYY #33 Travis Hafner (X - X - 24)
b1.new_ab()
b1.pitch_list("c d b")
b1.out("(F)F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #18 Hiroki Kuroda
t2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t2.new_ab()
t2.pitch_list("f b")
t2.out("P4")

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c c")
t2.hit(1)
t2.advance(3, "39 1B")

# 6. BOS #7  Stephen Drew (X - X - 12)
t2.new_ab()
t2.pitch_list("b c d")
t2.out("F7")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 12)
t2.new_ab()
t2.pitch_list("b b f b f")
t2.hit(1)

# 8. BOS #10 Jose Iglesias (12 - X - 39)
t2.new_ab()
t2.pitch_list("c")
t2.out("G1-3")


# Bot 2nd
# Pitching: BOS #11 Clay Buchholz
b2 = game.new_inning()

# 5. NYY #12 Vernon Wells (X - X - X)
b2.new_ab()
b2.pitch_list("b t b")
b2.out("G6-3")

# 6. NYY #36 Kevin Youkilis (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.out("G5-3")

# 7. NYY #31 Ichiro Suzuki (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)

# 8. NYY #17 Jayson Nix (X - X - 31)
b2.new_ab()
b2.pitch_list("1 1 s b")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #18 Hiroki Kuroda
t3 = game.new_inning()

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("f s b b")
t3.out("F8")

# 1. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b b")
t3.out("F8")

# 2. BOS #37 Mike Carp (X - X - X)
t3.new_ab()
t3.pitch_list("f f b s")
t3.out("K2-3")


# Bot 3rd
# Pitching: BOS #11 Clay Buchholz
b3 = game.new_inning()

# 9. NYY #53 Austin Romine (X - X - X)
b3.new_ab()
b3.pitch_list("c s b")
b3.hit(1)
b3.thrown_out(2, "24 DP5-6-3", 2, 11)

# 1. NYY #11 Brett Gardner (X - X - 53)
b3.new_ab()
b3.pitch_list("b s 1 f b b f")
b3.out("L6")

# 2. NYY #24 Robinson Canó (X - X - 53)
b3.new_ab()
b3.pitch_list("b b f")
b3.out("DP5-6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #18 Hiroki Kuroda
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("b f c f b b")
t4.hit(1)
t4.advance(3, "34 1B")
t4.advance(4, "12 FC6-4")

# 4. BOS #34 David Ortiz (X - X - 15)
t4.new_ab()
t4.pitch_list("1 b b b f f")
t4.hit(1)
t4.thrown_out(2, "12 FC6-4", 1, 18)

# 5. BOS #12 Mike Napoli (15 - X - 34)
t4.new_ab()
t4.reach("FC6-4", rbis=1)

# 6. BOS #7  Stephen Drew (X - X - 12)
t4.new_ab()
t4.pitch_list("c f b s")
t4.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 12)
t4.new_ab()
t4.pitch_list("c b s b b f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #11 Clay Buchholz
b4 = game.new_inning()

# 3. NYY #25 Mark Teixeira (X - X - X)
b4.new_ab()
b4.pitch_list("c f b s")
b4.out("K")

# 4. NYY #33 Travis Hafner (X - X - X)
b4.new_ab()
b4.pitch_list("c f c")
b4.out("!K")

# 5. NYY #12 Vernon Wells (X - X - X)
b4.new_ab()
b4.pitch_list("b f b")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #18 Hiroki Kuroda
t5 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
t5.new_ab()
t5.hit(4)

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("G3")

# 1. BOS #29 Daniel Nava (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)

# 2. BOS #37 Mike Carp (X - X - 29)
t5.new_ab()
t5.pitch_list("1 c b f 1 s")
t5.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
t5.new_ab()
t5.pitch_list("b")
t5.out("L9")


# Bot 5th
# Pitching: BOS #11 Clay Buchholz
b5 = game.new_inning()

# 6. NYY #36 Kevin Youkilis (X - X - X)
b5.new_ab()
b5.pitch_list("c b b f")
b5.out("G5-3")

# 7. NYY #31 Ichiro Suzuki (X - X - X)
b5.new_ab()
b5.out("G3-1")

# 8. NYY #17 Jayson Nix (X - X - X)
b5.new_ab()
b5.pitch_list("b c c b c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #18 Hiroki Kuroda
t6 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(4)

# 5. BOS #12 Mike Napoli (X - X - X)
t6.new_ab()
t6.pitch_list("c b c f")
t6.hit(1)
t6.thrown_out(2, "39 CS", 2, 48)

# 6. BOS #7  Stephen Drew (X - X - 12)
t6.new_ab()
t6.pitch_list("b b")
t6.out("F7")

# Pitching change (NYY): #48 Boone Logan replaces #18 Hiroki Kuroda
t6.pitching_substitution(48)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 12)
t6.new_ab()
t6.pitch_list("b s t s")
t6.out("K")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11, is_away_team=True)

# Loser team: NYY
# LP: NYY #18 Hiroki Kuroda
game.losing_pitcher(18)

# print(game)
game.generate_scorecard()
