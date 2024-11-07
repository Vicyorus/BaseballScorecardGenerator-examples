import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2013-07-20
# https://www.baseball-reference.com/boxes/BOS/BOS201307200.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2013/07/20/348194/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-07-20 16:26-19:59 (0:21 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "37,601",
        "temp": "93F, Cloudy",
        "wind": "18mph, Out To CF",
        "away": {
            "team": "New York Yankees",
            "starter": 18,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                31: "Ichiro Suzuki",
                24: "Robinson Canó",
                55: "Lyle Overbay",
                12: "Vernon Wells",
                33: "Travis Hafner",
                26: "Eduardo Núñez",
                19: "Chris Stewart",
                61: "Luis Alfonso Cruz",
                # Starting pitcher
                18: "Hiroki Kuroda",
                # Bench
                39: "Brent Lillibridge",
                53: "Austin Romine",
                60: "Melky Mesa",
                40: "Thomas Neal",
                # Bullpen
                65: "Phil Hughes",
                27: "Shawn Kelley",
                47: "Iván Nova",
                52: "CC Sabathia",
                38: "Preston Claiborne",
                48: "Boone Logan",
                43: "Adam Warren",
                42: "Mariano Rivera",
                46: "Andy Pettitte",
                62: "Joba Chamberlain",
                30: "David Robertson",
            },
            "lefties": [52, 48, 46],
            "lineup": [
                [11, "8"],
                [31, "9"],
                [24, "4"],
                [55, "3"],
                [12, "7"],
                [33, "0"],
                [26, "6"],
                [19, "2"],
                [61, "5"],
            ],
            "bench": [
                [39, "2B"],
                [53, "C"],
                [60, "LF"],
                [40, "LF"],
            ],
            "bullpen": [65, 27, 47, 52, 38, 48, 43, 42, 46, 62, 30],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                37: "Mike Carp",
                5: "Jonny Gomes",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                18: "Shane Victorino",
                12: "Mike Napoli",
                20: "Ryan Lavarnway",
                23: "Brandon Snyder",
                # Bullpen
                65: "Jose De La Torre",
                67: "Brandon Workman",
                32: "Craig Breslow",
                66: "Drake Britton",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                38: "Matt Thornton",
                54: "Pedro Beato",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [37, "3"],
                [5, "7"],
                [39, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [18, "CF"],
                [12, "1B"],
                [20, "C"],
                [23, "1B"],
            ],
            "bullpen": [65, 67, 32, 66, 31, 36, 19, 38, 54, 22, 46],
        },
        "umpires": {
            "HP": "Tim Welke",
            "1B": "Paul Emmel",
            "2B": "Dan Bellino",
            "3B": "Mike Everitt",
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
# Pitching: BOS #41 John Lackey
t1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t1.new_ab()
t1.pitch_list("b c b c")
t1.hit(1)
t1.thrown_out(1, "31 DP5-3", 2, 41)

# 2. NYY #31 Ichiro Suzuki (X - X - 11)
t1.new_ab()
t1.out("DP5-3")

# 3. NYY #24 Robinson Canó (X - X - X)
t1.new_ab()
t1.pitch_list("c f b c")
t1.out("!K")


# Bot 1st
# Pitching: NYY #18 Hiroki Kuroda
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.out("L8")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("c c b")
b1.reach("HBP")
b1.advance(2, "15 G1-3")
b1.thrown_out(4, "34 7-2", 3, 18)

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b1.new_ab()
b1.pitch_list("b b 1 b c f f")
b1.out("G1-3")

# 4. BOS #34 David Ortiz (X - 29 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.hit(1)


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 4. NYY #55 Lyle Overbay (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b f t")
t2.out("KT")

# 5. NYY #12 Vernon Wells (X - X - X)
t2.new_ab()
t2.pitch_list("f f")
t2.hit(1)
t2.advance(3, "26 2B")

# 6. NYY #33 Travis Hafner (X - X - 12)
t2.new_ab()
t2.pitch_list("c s s")
t2.out("K")

# 7. NYY #26 Eduardo Núñez (X - X - 12)
t2.new_ab()
t2.pitch_list("b d c")
t2.hit(2)

# 8. NYY #19 Chris Stewart (12 - 26 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b b")
t2.out("G6-3")


# Bot 2nd
# Pitching: NYY #18 Hiroki Kuroda
b2 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.out("F7")

# 6. BOS #5  Jonny Gomes (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G5-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("b c s b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 9. NYY #61 Luis Alfonso Cruz (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("F7")

# 1. NYY #11 Brett Gardner (X - X - X)
t3.new_ab()
t3.pitch_list("c b c")
t3.out("F8")

# 2. NYY #31 Ichiro Suzuki (X - X - X)
t3.new_ab()
t3.pitch_list("c b c b b")
t3.out("G2-3")


# Bot 3rd
# Pitching: NYY #18 Hiroki Kuroda
b3 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b3.new_ab()
b3.pitch_list("c c s")
b3.out("K")

# 9. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("c f f b f f b f f s")
b3.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.out("L9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 3. NYY #24 Robinson Canó (X - X - X)
t4.new_ab()
t4.pitch_list("b f f b b s")
t4.out("K")

# 4. NYY #55 Lyle Overbay (X - X - X)
t4.new_ab()
t4.hit(2)

# 5. NYY #12 Vernon Wells (X - 55 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("d c b f f s")
t4.out("K")

# 6. NYY #33 Travis Hafner (X - 55 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c")
t4.out("F8")


# Bot 4th
# Pitching: NYY #18 Hiroki Kuroda
b4 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("b f f b b")
b4.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 7. NYY #26 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)
t5.advance(2, "19 SB")
t5.advance(3, "19 SAC1-3")
t5.thrown_out(4, "61 FC6-2", 2, 41)

# 8. NYY #19 Chris Stewart (X - X - 26)
t5.new_ab(is_risp=True)
t5.pitch_list("c")
t5.out("SAC1-3")

# 9. NYY #61 Luis Alfonso Cruz (26 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b")
t5.reach("FC6-2")
t5.advance(2, "11 WP")
t5.advance(4, "11 1B")

# 1. NYY #11 Brett Gardner (X - X - 61)
t5.new_ab(is_risp=True)
t5.pitch_list("c c b f b b f")
t5.wp()
t5.hit(1, rbis=1)

# 2. NYY #31 Ichiro Suzuki (X - X - 11)
t5.new_ab()
t5.pitch_list("1")
t5.out("G4-3")


# Bot 5th
# Pitching: NYY #18 Hiroki Kuroda
b5 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(1)
b5.advance(2, "5 1B")
b5.advance(3, "7 G3")
b5.thrown_out(4, "10 2-1", 3, 18)

# 6. BOS #5  Jonny Gomes (X - X - 37)
b5.new_ab()
b5.pitch_list("1 b s f")
b5.hit(1)
b5.advance(2, "7 G3")

# 7. BOS #39 Jarrod Saltalamacchia (X - 37 - 5)
b5.new_ab(is_risp=True)
b5.pitch_list("b f s s")
b5.out("K")

# 8. BOS #7  Stephen Drew (X - 37 - 5)
b5.new_ab(is_risp=True)
b5.pitch_list("c")
b5.out("G3")

# 9. BOS #10 Jose Iglesias (37 - 5 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c f b")
b5.no_ab("2-1")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 3. NYY #24 Robinson Canó (X - X - X)
t6.new_ab()
t6.out("F8")

# 4. NYY #55 Lyle Overbay (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(2)

# 5. NYY #12 Vernon Wells (X - 55 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("f b f d s")
t6.out("K")

# 6. NYY #33 Travis Hafner (X - 55 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b d b c s c")
t6.out("!K")


# Bot 6th
# Pitching: NYY #18 Hiroki Kuroda
b6 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("c b l")
b6.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.error(4)
b6.reach("E4")
b6.advance(2, "29 WP")
b6.advance(3, "29 F8")

# 2. BOS #29 Daniel Nava (X - X - 2)
b6.new_ab(is_risp=True)
b6.pitch_list("b c 1 c f 1 b")
b6.wp()
b6.out("F8")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c b s")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 7. NYY #26 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.hit(2)
t7.advance(3, "19 G3-1")
t7.advance(4, "61 1B")

# 8. NYY #19 Chris Stewart (X - 26 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("s d")
t7.out("G3-1")

# 9. NYY #61 Luis Alfonso Cruz (26 - X - X)
t7.new_ab(is_risp=True)
t7.hit(1, rbis=1)
t7.advance(2, "11 1B")
t7.advance(3, "31 FC4-6")
t7.advance(4, "24 1B")

# 1. NYY #11 Brett Gardner (X - X - 61)
t7.new_ab()
t7.pitch_list("f b b")
t7.hit(1)
t7.thrown_out(2, "31 FC4-6", 2, 38)

# Pitching change (BOS): #38 Matt Thornton replaces #41 John Lackey
t7.pitching_substitution(38)

# 2. NYY #31 Ichiro Suzuki (X - 61 - 11)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.reach("FC4-6")
t7.advance(2, "24 1B")
t7.advance(4, "55 1B")

# 3. NYY #24 Robinson Canó (61 - X - 31)
t7.new_ab(is_risp=True)
t7.pitch_list("b f b c")
t7.hit(1, rbis=1)
t7.advance(3, "55 1B")

# 4. NYY #55 Lyle Overbay (X - 31 - 24)
t7.new_ab(is_risp=True)
t7.hit(1, rbis=1)

# 5. NYY #12 Vernon Wells (24 - X - 55)
t7.new_ab(is_risp=True)
t7.pitch_list("c f")
t7.out("G5-3")


# Bot 7th
# Pitching: NYY #18 Hiroki Kuroda
b7 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.hit(1)
b7.advance(3, "37 2B")
b7.advance(4, "5 SF8")

# 5. BOS #37 Mike Carp (X - X - 34)
b7.new_ab()
b7.pitch_list("f b")
b7.hit(2)
b7.advance(3, "39 G1-3")
b7.advance(4, "7 WP")

# 6. BOS #5  Jonny Gomes (34 - 37 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b c")
b7.out("SF8", rbis=1)

# 7. BOS #39 Jarrod Saltalamacchia (X - 37 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("d c t")
b7.out("G1-3")

# 8. BOS #7  Stephen Drew (37 - X - X)
b7.new_ab()
b7.pitch_list("b b f f b b")
b7.wp()
b7.reach("BB")

# 9. BOS #10 Jose Iglesias (X - X - 7)
b7.new_ab()
b7.pitch_list("c b s b 1 f")
b7.out("L4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #38 Matt Thornton
t8 = game.new_inning()

# 6. NYY #33 Travis Hafner (X - X - X)
t8.new_ab()
t8.out("G4-3")

# Pitching change (BOS): #54 Pedro Beato replaces #38 Matt Thornton
t8.pitching_substitution(54)

# 7. NYY #26 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("P6")

# 8. NYY #19 Chris Stewart (X - X - X)
t8.new_ab()
t8.pitch_list("b c b b c")
t8.out("F8")


# Bot 8th
# Pitching: NYY #30 David Robertson
b8 = game.new_inning()

# Pitching change (NYY): #30 David Robertson replaces #18 Hiroki Kuroda
b8.pitching_substitution(30)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G5-3")

# 2. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1)
b8.thrown_out(2, "15 DP2-4", 3, 30)

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b8.new_ab()
b8.pitch_list("c t")
b8.out("DP2-4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #54 Pedro Beato
t9 = game.new_inning()

# 9. NYY #61 Luis Alfonso Cruz (X - X - X)
t9.new_ab()
t9.pitch_list("c b f f")
t9.reach("HBP")
t9.advance(2, "11 E4")
t9.advance(3, "31 SB")
t9.advance("U", "24 SF8")

# 1. NYY #11 Brett Gardner (X - X - 61)
t9.new_ab()
t9.pitch_list("1 b")
t9.error(4)
t9.reach("E4")
t9.thrown_out(2, "55 CS", 3, 66)

# Pitching change (BOS): #66 Drake Britton replaces #54 Pedro Beato
t9.pitching_substitution(66)

# 2. NYY #31 Ichiro Suzuki (X - 61 - 11)
t9.new_ab(is_risp=True)
t9.pitch_list("b m 2")
t9.out("P6")

# 3. NYY #24 Robinson Canó (61 - X - 11)
t9.new_ab(is_risp=True)
t9.pitch_list("1 1 b b s b")
t9.out("SF8", rbis=1)

# 4. NYY #55 Lyle Overbay (X - X - 11)
t9.new_ab()
t9.pitch_list("c")
t9.no_ab("CS")


# Bot 9th
# Pitching: NYY #42 Mariano Rivera
b9 = game.new_inning()

# Pitching change (NYY): #42 Mariano Rivera replaces #30 David Robertson
b9.pitching_substitution(42)

# 4. BOS #34 David Ortiz (X - X - X)
b9.new_ab()
b9.out("(F)P5")

# 5. BOS #37 Mike Carp (X - X - X)
b9.new_ab()
b9.pitch_list("c f b")
b9.hit(1)

# 6. BOS #5  Jonny Gomes (X - X - 37)
b9.new_ab()
b9.pitch_list("f b f f s")
b9.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 37)
b9.new_ab()
b9.pitch_list("b c f b b t")
b9.out("KT")

# Winning team: NYY
# WP: NYY #18 Hiroki Kuroda
game.winning_pitcher(18, is_away_team=True)
# SV: NYY #42 Mariano Rivera
game.save_pitcher(42, is_away_team=True)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41)

# print(game)
game.generate_scorecard()
