import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2013-06-01
# https://www.baseball-reference.com/boxes/NYA/NYA201306010.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2013/06/01/347570/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-01 19:16-22:41",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "48,784",
        "temp": "86F, Partly Cloudy",
        "wind": "14mph, In From CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
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
                22: "Felix Doubront",
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
                11: "Clay Buchholz",
                19: "Koji Uehara",
                46: "Ryan Dempster",
            },
            "lefties": [22, 56, 30, 32, 31],
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
            "bullpen": [40, 41, 56, 30, 32, 31, 59, 36, 11, 19, 46],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 65,
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
                65: "Phil Hughes",
                # Bench
                53: "Austin Romine",
                40: "Reid Brignac",
                22: "Brennan Boesch",
                33: "Travis Hafner",
                55: "Lyle Overbay",
                # Bullpen
                18: "Hiroki Kuroda",
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
            "bullpen": [18, 27, 52, 38, 48, 41, 43, 42, 62, 30],
        },
        "umpires": {
            "HP": "Gary Cederstrom",
            "1B": "Vic Carapazza",
            "2B": "Chris Conroy",
            "3B": "Lance Barksdale",
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
# Pitching: NYY #65 Phil Hughes
t1 = game.new_inning()

# 1. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c f")
t1.out("G4-3")

# 2. BOS #37 Mike Carp (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")

# 3. BOS #15 Dustin Pedroia (X - X - 37)
t1.new_ab()
t1.pitch_list("c b")
t1.out("F8")

# 4. BOS #34 David Ortiz (X - X - 37)
t1.new_ab()
t1.pitch_list("b b f f 1 c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #22 Felix Doubront
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("c c b f f b")
b1.out("G4-3")

# 2. NYY #36 Kevin Youkilis (X - X - X)
b1.new_ab()
b1.pitch_list("c b b b b")
b1.reach("BB")
b1.advance(2, "25 1B")

# 3. NYY #24 Robinson Canó (X - X - 36)
b1.new_ab()
b1.pitch_list("b d b c")
b1.out("F9")

# 4. NYY #25 Mark Teixeira (X - X - 36)
b1.new_ab()
b1.pitch_list("c d b")
b1.hit(1)

# 5. NYY #12 Vernon Wells (X - 36 - 25)
b1.new_ab(is_risp=True)
b1.pitch_list("b c c f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #65 Phil Hughes
t2 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t2.new_ab()
t2.pitch_list("s b s f b f f f")
t2.hit(1)
t2.advance(2, "7 WP")

# 6. BOS #7  Stephen Drew (X - X - 12)
t2.new_ab(is_risp=True)
t2.pitch_list("b c f b f")
t2.wp()
t2.out("P5")

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - X)
t2.new_ab(is_risp=True)
t2.out("F9")

# 8. BOS #10 Jose Iglesias (X - 12 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("c s s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #22 Felix Doubront
b2 = game.new_inning()

# 6. NYY #17 Jayson Nix (X - X - X)
b2.new_ab()
b2.pitch_list("b b c b b")
b2.reach("BB")
b2.thrown_out(2, "39 DP4-6-3", 1, 22)

# 7. NYY #39 David Adams (X - X - 17)
b2.new_ab()
b2.pitch_list("1 s c f")
b2.out("DP4-6-3")

# 8. NYY #31 Ichiro Suzuki (X - X - X)
b2.new_ab()
b2.pitch_list("c b c f b")
b2.hit(1)
b2.advance(2, "19 BB")

# 9. NYY #19 Chris Stewart (X - X - 31)
b2.new_ab()
b2.pitch_list("1 1 b b 1 b b")
b2.reach("BB")

# 1. NYY #11 Brett Gardner (X - 31 - 19)
b2.new_ab(is_risp=True)
b2.pitch_list("c c d")
b2.out("G2-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #65 Phil Hughes
t3 = game.new_inning()

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b f b")
t3.hit(2)
t3.advance(3, "29 1B")
t3.advance(4, "37 2B")

# 1. BOS #29 Daniel Nava (X - 44 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f b f f")
t3.hit(1)
t3.advance(3, "37 2B")
t3.advance(4, "12 HR")

# 2. BOS #37 Mike Carp (44 - X - 29)
t3.new_ab(is_risp=True)
t3.pitch_list("f 1 f 1")
t3.hit(2, rbis=1)
t3.advance(4, "12 HR")

# 3. BOS #15 Dustin Pedroia (29 - 37 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c b f f s")
t3.out("K")

# 4. BOS #34 David Ortiz (29 - 37 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("i i i i")
t3.reach("IBB")
t3.advance(4, "12 HR")

# 5. BOS #12 Mike Napoli (29 - 37 - 34)
t3.new_ab(is_risp=True)
t3.pitch_list("s c f b b")
t3.hit(4, rbis=4)

# 6. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("c f s")
t3.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t3.new_ab()
t3.pitch_list("f s b b f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #22 Felix Doubront
b3 = game.new_inning()

# 2. NYY #36 Kevin Youkilis (X - X - X)
b3.new_ab()
b3.pitch_list("c b f c")
b3.out("!K")

# 3. NYY #24 Robinson Canó (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.hit(1)
b3.thrown_out(2, "12 FC5-4", 3, 22)

# 4. NYY #25 Mark Teixeira (X - X - 24)
b3.new_ab()
b3.pitch_list("c s c")
b3.out("!K")

# 5. NYY #12 Vernon Wells (X - X - 24)
b3.new_ab()
b3.reach("FC5-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #65 Phil Hughes
t4 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
t4.new_ab()
t4.pitch_list("c b c f f")
t4.out("G6-3")

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("F9")

# 1. BOS #29 Daniel Nava (X - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.hit(1)

# 2. BOS #37 Mike Carp (X - X - 29)
t4.new_ab()
t4.pitch_list("f b c b c")
t4.out("!K")


# Bot 4th
# Pitching: BOS #22 Felix Doubront
b4 = game.new_inning()

# 6. NYY #17 Jayson Nix (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.advance(2, "39 1B")
b4.advance(3, "31 FC3-6")
b4.advance(4, "19 SF8")

# 7. NYY #39 David Adams (X - X - 17)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)
b4.thrown_out(2, "31 FC3-6", 1, 22)

# 8. NYY #31 Ichiro Suzuki (X - 17 - 39)
b4.new_ab(is_risp=True)
b4.pitch_list("l b")
b4.reach("FC3-6")

# 9. NYY #19 Chris Stewart (17 - X - 31)
b4.new_ab(is_risp=True)
b4.pitch_list("b b")
b4.out("SF8", rbis=1)

# 1. NYY #11 Brett Gardner (X - X - 31)
b4.new_ab()
b4.pitch_list("1 f s b f 1 t")
b4.out("KT")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #65 Phil Hughes
t5 = game.new_inning()

# Defensive change (NYY): #53 Austin Romine replaces #19 Chris Stewart (C), playing C, batting 9th
t5.defensive_substitution(9, 53, "2")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t5.new_ab()
t5.pitch_list("f f")
t5.hit(1)
t5.advance(2, "7 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
t5.new_ab()
t5.pitch_list("b c f b f f c")
t5.out("!K")

# Pitching change (NYY): #38 Preston Claiborne replaces #65 Phil Hughes
t5.pitching_substitution(38)

# 5. BOS #12 Mike Napoli (X - X - 15)
t5.new_ab()
t5.pitch_list("b b c c f f 1 s")
t5.out("K")

# 6. BOS #7  Stephen Drew (X - X - 15)
t5.new_ab()
t5.hit(1)

# 7. BOS #39 Jarrod Saltalamacchia (X - 15 - 7)
t5.new_ab(is_risp=True)
t5.pitch_list("c s b c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #22 Felix Doubront
b5 = game.new_inning()

# 2. NYY #36 Kevin Youkilis (X - X - X)
b5.new_ab()
b5.pitch_list("b b f f s")
b5.out("K")

# 3. NYY #24 Robinson Canó (X - X - X)
b5.new_ab()
b5.pitch_list("s b f b b")
b5.out("G4-3")

# 4. NYY #25 Mark Teixeira (X - X - X)
b5.new_ab()
b5.pitch_list("b s b c s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #38 Preston Claiborne
t6 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
t6.new_ab()
t6.pitch_list("s")
t6.out("G4-3")

# 9. BOS #44 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("b c b s")
t6.out("G3")

# 1. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("c f b")
t6.hit(1)
t6.advance(2, "37 1B")

# 2. BOS #37 Mike Carp (X - X - 29)
t6.new_ab()
t6.pitch_list("1 b")
t6.hit(1)

# 3. BOS #15 Dustin Pedroia (X - 29 - 37)
t6.new_ab(is_risp=True)
t6.pitch_list("c b")
t6.out("F9")


# Bot 6th
# Pitching: BOS #22 Felix Doubront
b6 = game.new_inning()

# 5. NYY #12 Vernon Wells (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("P4")

# 6. NYY #17 Jayson Nix (X - X - X)
b6.new_ab()
b6.pitch_list("b b s")
b6.out("F8")

# 7. NYY #39 David Adams (X - X - X)
b6.new_ab()
b6.pitch_list("f b")
b6.hit(1)

# 8. NYY #31 Ichiro Suzuki (X - X - 39)
b6.new_ab()
b6.pitch_list("c s")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #43 Adam Warren
t7 = game.new_inning()

# Pitching change (NYY): #43 Adam Warren replaces #38 Preston Claiborne
t7.pitching_substitution(43)

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("c b f b b b")
t7.reach("BB")
t7.advance(2, "12 1B")
t7.advance(3, "7 DP4-6-3")

# 5. BOS #12 Mike Napoli (X - X - 34)
t7.new_ab()
t7.pitch_list("b b b s s f")
t7.hit(1)
t7.thrown_out(2, "7 DP4-6-3", 1, 43)

# 6. BOS #7  Stephen Drew (X - 34 - 12)
t7.new_ab(is_risp=True)
t7.out("DP4-6-3")

# 7. BOS #39 Jarrod Saltalamacchia (34 - X - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #22 Felix Doubront
b7.pitching_substitution(36)

# Defensive change (BOS): #5 Jonny Gomes replaces #37 Mike Carp (RF), playing RF, batting 2nd
b7.defensive_substitution(2, 5, "9")

# 9. NYY #53 Austin Romine (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b f")
b7.out("G5-3")

# 1. NYY #11 Brett Gardner (X - X - X)
b7.new_ab()
b7.pitch_list("c c f b f b")
b7.out("F7")

# 2. NYY #36 Kevin Youkilis (X - X - X)
b7.new_ab()
b7.pitch_list("c s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #43 Adam Warren
t8 = game.new_inning()

# 8. BOS #10 Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("b c f b b")
t8.hit(1)
t8.advance(3, "44 1B")
t8.advance(4, "29 HR")

# 9. BOS #44 Jackie Bradley Jr. (X - X - 10)
t8.new_ab()
t8.pitch_list("c b c d")
t8.hit(1)
t8.advance(4, "29 HR")

# 1. BOS #29 Daniel Nava (10 - X - 44)
t8.new_ab(is_risp=True)
t8.pitch_list("f s f")
t8.hit(4, rbis=3)

# 2. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("L3")

# 4. BOS #34 David Ortiz (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b b f f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #36 Junichi Tazawa
b8.pitching_substitution(32)

# 3. NYY #24 Robinson Canó (X - X - X)
b8.new_ab()
b8.out("G4-3")

# 4. NYY #25 Mark Teixeira (X - X - X)
b8.new_ab()
b8.pitch_list("c s b s")
b8.out("K")

# 5. NYY #12 Vernon Wells (X - X - X)
b8.new_ab()
b8.pitch_list("b c s")
b8.out("G5-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #43 Adam Warren
t9 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("b c s f b s")
t9.out("K")

# 6. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.hit(4)

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t9.new_ab()
t9.pitch_list("s b")
t9.hit(2)
t9.advance(4, "10 1B")

# 8. BOS #10 Jose Iglesias (X - 39 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c b b c f")
t9.hit(1, rbis=1)
t9.advance(3, "44 2B")
t9.advance(4, "29 G6-3")

# 9. BOS #44 Jackie Bradley Jr. (X - X - 10)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(2)

# 1. BOS #29 Daniel Nava (10 - 44 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("f f")
t9.out("G6-3", rbis=1)

# 2. BOS #5  Jonny Gomes (X - 44 - X)
t9.new_ab(is_risp=True)
t9.out("G1-3")


# Bot 9th
# Pitching: BOS #19 Koji Uehara
b9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
b9.pitching_substitution(19)

# 6. NYY #17 Jayson Nix (X - X - X)
b9.new_ab()
b9.pitch_list("c b s s")
b9.out("K")

# 7. NYY #39 David Adams (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("F9")

# 8. NYY #31 Ichiro Suzuki (X - X - X)
b9.new_ab()
b9.pitch_list("b b c s f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #22 Felix Doubront
game.winning_pitcher(22, is_away_team=True)

# Loser team: NYY
# LP: NYY #65 Phil Hughes
game.losing_pitcher(65)

# print(game)
game.generate_scorecard()
