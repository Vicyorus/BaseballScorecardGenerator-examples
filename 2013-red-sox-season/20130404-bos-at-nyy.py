import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2013-04-04
# https://www.baseball-reference.com/boxes/NYA/NYA201304040.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2013/04/04/346779/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-04-04 19:08-21:46",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "40,611",
        "temp": "43F, Partly Cloudy",
        "wind": "14mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                16: "Will Middlebrooks",
                44: "Jackie Bradley Jr.",
                3: "David Ross",
                10: "Jose Iglesias",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                29: "Daniel Nava",
                23: "Pedro Ciriaco",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                30: "Andrew Miller",
                91: "Alfredo Aceves",
                52: "Joel Hanrahan",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
            },
            "lefties": [30, 31, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [12, "3"],
                [5, "0"],
                [16, "5"],
                [44, "7"],
                [3, "2"],
                [10, "6"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [29, "LF"],
                [23, "3B"],
            ],
            "bullpen": [40, 41, 30, 91, 52, 31, 59, 36, 11, 19, 22],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 46,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                24: "Robinson Canó",
                36: "Kevin Youkilis",
                33: "Travis Hafner",
                12: "Vernon Wells",
                31: "Ichiro Suzuki",
                26: "Eduardo Núñez",
                55: "Lyle Overbay",
                29: "Francisco Cervelli",
                # Starting pitcher
                46: "Andy Pettitte",
                # Bench
                19: "Chris Stewart",
                17: "Jayson Nix",
                22: "Brennan Boesch",
                45: "Ben Francisco",
                # Bullpen
                18: "Hiroki Kuroda",
                27: "Shawn Kelley",
                47: "Iván Nova",
                52: "CC Sabathia",
                48: "Boone Logan",
                41: "David Phelps",
                43: "Adam Warren",
                42: "Mariano Rivera",
                62: "Joba Chamberlain",
                38: "Cody Eppley",
                30: "David Robertson",
            },
            "lefties": [46, 52, 48],
            "lineup": [
                [11, "8"],
                [24, "4"],
                [36, "5"],
                [33, "0"],
                [12, "7"],
                [31, "9"],
                [26, "6"],
                [55, "3"],
                [29, "2"],
            ],
            "bench": [
                [19, "C"],
                [17, "3B"],
                [22, "RF"],
                [45, "LF"],
            ],
            "bullpen": [18, 27, 47, 52, 48, 41, 43, 42, 62, 38, 30],
        },
        "umpires": {
            "HP": "Mike DiMuro",
            "1B": "Dan Bellino",
            "2B": "Ted Barrett",
            "3B": "Alfonso Márquez",
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
# Pitching: NYY #46 Andy Pettitte
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c c")
t1.out("F8")

# 2. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("c b s")
t1.hit(1)
t1.advance(2, "12 1B")
t1.thrown_out(4, "5 WP", 3, 46)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t1.new_ab()
t1.pitch_list("c")
t1.out("F9")

# 4. BOS #12 Mike Napoli (X - X - 18)
t1.new_ab()
t1.hit(1)
t1.advance(2, "5 WP")

# 5. BOS #5  Jonny Gomes (X - 18 - 12)
t1.new_ab(is_risp=True)
t1.pitch_list("b")


# Bot 1st
# Pitching: BOS #46 Ryan Dempster
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b b b")
b1.reach("BB")
b1.thrown_out(2, "24 CS", 1, 46)

# 2. NYY #24 Robinson Canó (X - X - 11)
b1.new_ab()
b1.pitch_list("c b b b s")
b1.out("G5-3")

# 3. NYY #36 Kevin Youkilis (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b f")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #46 Andy Pettitte
t2 = game.new_inning()

# 6. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("b f b c")
t2.out("P4")

# 7. BOS #44 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.hit(1)
t2.thrown_out(2, "3 DP4-6-3", 2, 46)

# 8. BOS #3  David Ross (X - X - 16)
t2.new_ab()
t2.pitch_list("b")
t2.out("DP4-6-3")


# Bot 2nd
# Pitching: BOS #46 Ryan Dempster
b2 = game.new_inning()

# 4. NYY #33 Travis Hafner (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f")
b2.hit(1)
b2.advance(3, "26 2B")
b2.advance(4, "55 1B")

# 5. NYY #12 Vernon Wells (X - X - 33)
b2.new_ab()
b2.pitch_list("f s s")
b2.out("K")

# 6. NYY #31 Ichiro Suzuki (X - X - 33)
b2.new_ab()
b2.pitch_list("c b c s")
b2.out("K")

# 7. NYY #26 Eduardo Núñez (X - X - 33)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(2)
b2.advance(4, "55 1B")

# 8. NYY #55 Lyle Overbay (33 - 26 - X)
b2.new_ab(is_risp=True)
b2.hit(1, rbis=2)

# 9. NYY #29 Francisco Cervelli (X - X - 55)
b2.new_ab()
b2.pitch_list("b s c b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #46 Andy Pettitte
t3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
t3.new_ab()
t3.hit(1)
t3.thrown_out(2, "2 DP1-6-3", 1, 46)

# 1. BOS #2  Jacoby Ellsbury (X - X - 3)
t3.new_ab()
t3.pitch_list("f")
t3.out("DP1-6-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b")
t3.out("G1-3")


# Bot 3rd
# Pitching: BOS #46 Ryan Dempster
b3 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b3.new_ab()
b3.hit(4)

# 2. NYY #24 Robinson Canó (X - X - X)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")

# 3. NYY #36 Kevin Youkilis (X - X - 24)
b3.new_ab()
b3.pitch_list("c f f s")
b3.out("K")

# 4. NYY #33 Travis Hafner (X - X - 24)
b3.new_ab()
b3.pitch_list("f s 1 b b b s")
b3.out("K")

# 5. NYY #12 Vernon Wells (X - X - 24)
b3.new_ab()
b3.pitch_list("b b s d")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #46 Andy Pettitte
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("L6")

# 4. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("b f b b b")
t4.reach("BB")

# 5. BOS #5  Jonny Gomes (X - X - 15)
t4.new_ab()
t4.pitch_list("c 1 s d 1 b s")
t4.out("K")

# 6. BOS #16 Will Middlebrooks (X - X - 15)
t4.new_ab()
t4.out("G4-3")


# Bot 4th
# Pitching: BOS #46 Ryan Dempster
b4 = game.new_inning()

# 6. NYY #31 Ichiro Suzuki (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s f b b")
b4.reach("BB")
b4.thrown_out(2, "26 FC5-4", 1, 46)

# 7. NYY #26 Eduardo Núñez (X - X - 31)
b4.new_ab()
b4.pitch_list("c c 1 f b b")
b4.reach("FC5-4")
b4.advance(2, "29 BB")

# 8. NYY #55 Lyle Overbay (X - X - 26)
b4.new_ab()
b4.pitch_list("c c s")
b4.out("K")

# 9. NYY #29 Francisco Cervelli (X - X - 26)
b4.new_ab()
b4.pitch_list("c 1 b f b b f b")
b4.reach("BB")

# 1. NYY #11 Brett Gardner (X - 26 - 29)
b4.new_ab(is_risp=True)
b4.pitch_list("c d c b b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #46 Andy Pettitte
t5 = game.new_inning()

# 7. BOS #44 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b c b b f")
t5.out("G5-3")

# 8. BOS #3  David Ross (X - X - X)
t5.new_ab()
t5.pitch_list("f f b")
t5.out("G5-3")

# 9. BOS #10 Jose Iglesias (X - X - X)
t5.new_ab()
t5.pitch_list("b c f s")
t5.out("K")


# Bot 5th
# Pitching: BOS #46 Ryan Dempster
b5 = game.new_inning()

# 2. NYY #24 Robinson Canó (X - X - X)
b5.new_ab()
b5.out("G3-1")

# 3. NYY #36 Kevin Youkilis (X - X - X)
b5.new_ab()
b5.pitch_list("b b c")
b5.hit(2)

# 4. NYY #33 Travis Hafner (X - 36 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b f c s")
b5.out("K")

# 5. NYY #12 Vernon Wells (X - 36 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c b c")
b5.out("G2")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #46 Andy Pettitte
t6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.thrown_out(2, "12 FC6-4", 3, 46)

# 2. BOS #18 Shane Victorino (X - X - 10)
t6.new_ab()
t6.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - 10)
t6.new_ab()
t6.pitch_list("c b b b")
t6.out("F8")

# 4. BOS #12 Mike Napoli (X - X - 10)
t6.new_ab()
t6.pitch_list("b b c c")
t6.reach("FC6-4")


# Bot 6th
# Pitching: BOS #36 Junichi Tazawa
b6 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #46 Ryan Dempster
b6.pitching_substitution(36)

# 6. NYY #31 Ichiro Suzuki (X - X - X)
b6.new_ab()
b6.out("(F)F7")

# 7. NYY #26 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c f b")
b6.hit(1)
b6.thrown_out(2, "55 CS", 2, 36)

# 8. NYY #55 Lyle Overbay (X - X - 26)
b6.new_ab()
b6.pitch_list("c s b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #46 Andy Pettitte
t7 = game.new_inning()

# 5. BOS #5  Jonny Gomes (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("F9")

# 6. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("c s b f s")
t7.out("K")

# 7. BOS #44 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.advance(4, "3 2B")

# 8. BOS #3  David Ross (X - X - 16)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(2, rbis=1)

# 9. BOS #10 Jose Iglesias (X - 44 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c s d")
t7.out("F8")


# Bot 7th
# Pitching: BOS #59 Clayton Mortensen
b7 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #36 Junichi Tazawa
b7.pitching_substitution(59)

# 9. NYY #29 Francisco Cervelli (X - X - X)
b7.new_ab()
b7.pitch_list("s b b b")
b7.hit(4)

# 1. NYY #11 Brett Gardner (X - X - X)
b7.new_ab()
b7.pitch_list("b f c f")
b7.hit(1)
b7.thrown_out(2, "9-6", 1, 59)

# 2. NYY #24 Robinson Canó (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G5-3")

# 3. NYY #36 Kevin Youkilis (X - X - X)
b7.new_ab()
b7.pitch_list("c f b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #46 Andy Pettitte
t8 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.thrown_out(2, "18 DP3-6-3", 1, 46)

# 2. BOS #18 Shane Victorino (X - X - 10)
t8.new_ab()
t8.pitch_list("b")
t8.out("DP3-6-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("b c s b f")
t8.out("G6-3")


# Bot 8th
# Pitching: BOS #59 Clayton Mortensen
b8 = game.new_inning()

# 4. NYY #33 Travis Hafner (X - X - X)
b8.new_ab()
b8.pitch_list("b c f b b")
b8.out("F8")

# 5. NYY #12 Vernon Wells (X - X - X)
b8.new_ab()
b8.out("L6")

# 6. NYY #31 Ichiro Suzuki (X - X - X)
b8.new_ab()
b8.pitch_list("c s b")
b8.out("G3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #42 Mariano Rivera
t9 = game.new_inning()

# Pitching change (NYY): #42 Mariano Rivera replaces #46 Andy Pettitte
t9.pitching_substitution(42)

# 4. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("c b f b b f b")
t9.reach("BB")
t9.advance(3, "16 2B")
t9.advance(4, "44 G3-1")

# 5. BOS #5  Jonny Gomes (X - X - 15)
t9.new_ab()
t9.pitch_list("s b s")
t9.out("F9")

# 6. BOS #16 Will Middlebrooks (X - X - 15)
t9.new_ab()
t9.pitch_list("c")
t9.hit(2)
t9.advance(3, "44 G3-1")

# 7. BOS #44 Jackie Bradley Jr. (15 - 5 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("f c b")
t9.out("G3-1", rbis=1)

# 8. BOS #3  David Ross (5 - X - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c f c")
t9.out("!K")

# Winning team: NYY
# WP: NYY #46 Andy Pettitte
game.winning_pitcher(46)
# SV: NYY #42 Mariano Rivera
game.save_pitcher(42)

# Loser team: BOS
# LP: BOS #46 Ryan Dempster
game.losing_pitcher(46, is_away_team=True)

# print(game)
game.generate_scorecard()
