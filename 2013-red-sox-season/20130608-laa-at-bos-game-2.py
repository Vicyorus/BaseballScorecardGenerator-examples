import os
from baseball_scorecard.baseball_scorecard import Scorecard

# LAA @ BOS, 2013-06-08
# https://www.baseball-reference.com/boxes/BOS/BOS201306082.shtml
# https://www.mlb.com/gameday/angels-vs-red-sox/2013/06/08/347664/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-08 19:17-22:42",
        "at": "Fenway Park, Boston, MA",
        "att": "36,518",
        "temp": "77F, Partly Cloudy",
        "wind": "12mph, Out To RF",
        "away": {
            "team": "Los Angeles Angels",
            "starter": 33,
            "roster": {
                # Lineup
                27: "Mike Trout",
                32: "Josh Hamilton",
                5: "Albert Pujols",
                44: "Mark Trumbo",
                47: "Howie Kendrick",
                10: "Brad Hawpe",
                6: "Alberto Callaspo",
                16: "Hank Conger",
                2: "Erick Aybar",
                # Starting pitcher
                33: "C.J. Wilson",
                # Bench
                17: "Chris Iannetta",
                8: "Chris Nelson",
                20: "Brendan Harris",
                39: "JB Shuck",
                # Bullpen
                55: "Joe Blanton",
                49: "Ernesto Frieri",
                40: "Kevin Jepsen",
                58: "Michael Kohn",
                37: "Scott Downs",
                57: "Jerome Williams",
                48: "Tommy Hanson",
                36: "Jered Weaver",
                59: "Robert Coello",
                60: "Jason Vargas",
            },
            "lefties": [33, 37, 60],
            "lineup": [
                [27, "8"],
                [32, "9"],
                [5, "0"],
                [44, "3"],
                [47, "4"],
                [10, "7"],
                [6, "5"],
                [16, "2"],
                [2, "6"],
            ],
            "bench": [
                [17, "C"],
                [8, "3B"],
                [20, "SS"],
                [39, "LF"],
            ],
            "bullpen": [55, 49, 40, 58, 37, 57, 48, 36, 59, 60],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 11,
            "roster": {
                # Lineup
                18: "Shane Victorino",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                3: "David Ross",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                11: "Clay Buchholz",
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
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [18, "8"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [3, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [2, "CF"],
                [39, "C"],
                [37, "1B"],
                [23, "3B"],
            ],
            "bullpen": [40, 41, 56, 30, 32, 31, 59, 36, 19, 22, 46],
        },
        "umpires": {
            "HP": "Marvin Hudson",
            "1B": "Marty Foster",
            "2B": "Wally Bell",
            "3B": "Clint Fagan",
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
# Pitching: BOS #11 Clay Buchholz
t1 = game.new_inning()

# 1. LAA #27 Mike Trout (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("P5")

# 2. LAA #32 Josh Hamilton (X - X - X)
t1.new_ab()
t1.pitch_list("s f")
t1.out("G4-3")

# 3. LAA #5  Albert Pujols (X - X - X)
t1.new_ab()
t1.out("P4")


# Bot 1st
# Pitching: LAA #33 C.J. Wilson
b1 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.advance(4, "5 2B")

# 2. BOS #5  Jonny Gomes (X - X - 18)
b1.new_ab()
b1.pitch_list("b 1 c")
b1.hit(2, rbis=1)
b1.advance(4, "15 2B")

# 3. BOS #15 Dustin Pedroia (X - 5 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c b")
b1.hit(2, rbis=1)
b1.advance(3, "3 BB")

# 4. BOS #34 David Ortiz (X - 15 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b s b")
b1.out("F7")

# 5. BOS #12 Mike Napoli (X - 15 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c s b s")
b1.out("K")

# 6. BOS #29 Daniel Nava (X - 15 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("d f b c b b")
b1.reach("BB")
b1.advance(2, "3 BB")

# 7. BOS #3  David Ross (X - 15 - 29)
b1.new_ab(is_risp=True)
b1.pitch_list("b b f b b")
b1.reach("BB")

# 8. BOS #7  Stephen Drew (15 - 29 - 3)
b1.new_ab(is_risp=True)
b1.pitch_list("c b f b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #11 Clay Buchholz
t2 = game.new_inning()

# 4. LAA #44 Mark Trumbo (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b b s")
t2.out("K")

# 5. LAA #47 Howie Kendrick (X - X - X)
t2.new_ab()
t2.pitch_list("b c b f")
t2.hit(1)

# 6. LAA #10 Brad Hawpe (X - X - 47)
t2.new_ab()
t2.pitch_list("1 s b c 1 c")
t2.out("!K")

# 7. LAA #6  Alberto Callaspo (X - X - 47)
t2.new_ab()
t2.pitch_list("c")
t2.out("F9")


# Bot 2nd
# Pitching: LAA #33 C.J. Wilson
b2 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b2.new_ab()
b2.pitch_list("b b c")
b2.out("G5-3")

# 1. BOS #18 Shane Victorino (X - X - X)
b2.new_ab()
b2.pitch_list("c b l")
b2.out("G5-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c c")
b2.hit(1)
b2.advance(2, "15 BB")
b2.advance(4, "34 2B")

# 3. BOS #15 Dustin Pedroia (X - X - 5)
b2.new_ab()
b2.pitch_list("1 b s b d 1 b")
b2.reach("BB")
b2.advance(3, "34 2B")

# 4. BOS #34 David Ortiz (X - 5 - 15)
b2.new_ab(is_risp=True)
b2.hit(2, rbis=1)

# 5. BOS #12 Mike Napoli (15 - 34 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c b c s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #11 Clay Buchholz
t3 = game.new_inning()

# 8. LAA #16 Hank Conger (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(2)
t3.advance(3, "2 G3-1")
t3.advance(4, "27 1B")

# 9. LAA #2  Erick Aybar (X - 16 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b c f f f d f f f")
t3.out("G3-1")

# 1. LAA #27 Mike Trout (16 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f")
t3.hit(1, rbis=1)
t3.advance(2, "5 BB")

# 2. LAA #32 Josh Hamilton (X - X - 27)
t3.new_ab()
t3.out("L9")

# 3. LAA #5  Albert Pujols (X - X - 27)
t3.new_ab()
t3.pitch_list("1 b b b c s f 1 b")
t3.reach("BB")

# 4. LAA #44 Mark Trumbo (X - 27 - 5)
t3.new_ab(is_risp=True)
t3.pitch_list("c b s")
t3.out("F8")


# Bot 3rd
# Pitching: LAA #33 C.J. Wilson
b3 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b3.new_ab()
b3.pitch_list("b c b c f f f")
b3.hit(1)
b3.advance(2, "3 SAC5-3")

# 7. BOS #3  David Ross (X - X - 29)
b3.new_ab()
b3.out("SAC5-3")

# 8. BOS #7  Stephen Drew (X - 29 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c f b f b f b c")
b3.out("!K")

# 9. BOS #10 Jose Iglesias (X - 29 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c c d b")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #11 Clay Buchholz
t4 = game.new_inning()

# 5. LAA #47 Howie Kendrick (X - X - X)
t4.new_ab()
t4.pitch_list("c c f")
t4.out("F8")

# 6. LAA #10 Brad Hawpe (X - X - X)
t4.new_ab()
t4.pitch_list("s s f b b f f f s")
t4.out("K")

# 7. LAA #6  Alberto Callaspo (X - X - X)
t4.new_ab()
t4.pitch_list("b c c")
t4.out("G1")


# Bot 4th
# Pitching: LAA #33 C.J. Wilson
b4 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
b4.new_ab()
b4.pitch_list("c f")
b4.out("F7")

# 2. BOS #5  Jonny Gomes (X - X - X)
b4.new_ab()
b4.pitch_list("c b b c")
b4.out("G5-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #11 Clay Buchholz
t5 = game.new_inning()

# 8. LAA #16 Hank Conger (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F7")

# 9. LAA #2  Erick Aybar (X - X - X)
t5.new_ab()
t5.pitch_list("f b")
t5.out("G4-3")

# 1. LAA #27 Mike Trout (X - X - X)
t5.new_ab()
t5.pitch_list("c b s")
t5.out("F8")


# Bot 5th
# Pitching: LAA #33 C.J. Wilson
b5 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G5-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("c c b")
b5.hit(1)
b5.error(5)
b5.advance(2, "E5")
b5.advance("U", "3 1B")

# 6. BOS #29 Daniel Nava (X - 12 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b 2")
b5.out("F9")

# 7. BOS #3  David Ross (X - 12 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("s d b")
b5.hit(1, rbis=1)

# 8. BOS #7  Stephen Drew (X - X - 3)
b5.new_ab()
b5.pitch_list("f c f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #11 Clay Buchholz
t6 = game.new_inning()

# 2. LAA #32 Josh Hamilton (X - X - X)
t6.new_ab()
t6.pitch_list("f s")
t6.hit(2)
t6.advance(3, "5 G6-3")
t6.advance(4, "44 SF9")

# 3. LAA #5  Albert Pujols (X - 32 - X)
t6.new_ab(is_risp=True)
t6.out("G6-3")

# 4. LAA #44 Mark Trumbo (32 - X - X)
t6.new_ab(is_risp=True)
t6.out("SF9", rbis=1)

# 5. LAA #47 Howie Kendrick (X - X - X)
t6.new_ab()
t6.pitch_list("f s")
t6.hit(1)

# 6. LAA #10 Brad Hawpe (X - X - 47)
t6.new_ab()
t6.pitch_list("b 1 b s c c")
t6.out("!K")


# Bot 6th
# Pitching: LAA #57 Jerome Williams
b6 = game.new_inning()

# Pitching change (LAA): #57 Jerome Williams replaces #33 C.J. Wilson
b6.pitching_substitution(57)

# 9. BOS #10 Jose Iglesias (X - X - X)
b6.new_ab()
b6.pitch_list("b b c")
b6.hit(1)
b6.error(3)
b6.advance(2, "18 POE3")
b6.advance(3, "15 PB")
b6.advance(4, "15 1B")

# 1. BOS #18 Shane Victorino (X - X - 10)
b6.new_ab(is_risp=True)
b6.pitch_list("1 c b s b f 2 d s")
b6.out("K")

# 2. BOS #5  Jonny Gomes (X - 10 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.out("P4")

# 3. BOS #15 Dustin Pedroia (X - 10 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b b b c f")
b6.pb()
b6.hit(1, rbis=1)
b6.advance(4, "34 HR")

# 4. BOS #34 David Ortiz (X - X - 15)
b6.new_ab()
b6.pitch_list("c 1")
b6.hit(4, rbis=2)

# 5. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #11 Clay Buchholz
t7 = game.new_inning()

# 7. LAA #6  Alberto Callaspo (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b")
t7.out("L4")

# 8. LAA #16 Hank Conger (X - X - X)
t7.new_ab()
t7.pitch_list("c b f")
t7.hit(1)
t7.thrown_out(2, "2 FC4-6", 2, 11)

# 9. LAA #2  Erick Aybar (X - X - 16)
t7.new_ab()
t7.pitch_list("f f b 1 f")
t7.reach("FC4-6")

# Pitching change (BOS): #32 Craig Breslow replaces #11 Clay Buchholz
t7.pitching_substitution(32)

# 1. LAA #27 Mike Trout (X - X - 2)
t7.new_ab()
t7.pitch_list("b c f f")
t7.out("G5-3")


# Bot 7th
# Pitching: LAA #57 Jerome Williams
b7 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("b c s t")
b7.out("KT")

# 7. BOS #3  David Ross (X - X - X)
b7.new_ab()
b7.pitch_list("c c b")
b7.out("F8")

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.hit(1)
b7.advance(3, "10 1B")

# 9. BOS #10 Jose Iglesias (X - X - 7)
b7.new_ab()
b7.pitch_list("b c c")
b7.hit(1)
b7.advance(2, "18 SB")

# 1. BOS #18 Shane Victorino (7 - X - 10)
b7.new_ab(is_risp=True)
b7.pitch_list("f b s 1 p f b f")
b7.out("G3-1")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# 2. LAA #32 Josh Hamilton (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.out("G4-3")

# 3. LAA #5  Albert Pujols (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("F8")

# 4. LAA #44 Mark Trumbo (X - X - X)
t8.new_ab()
t8.pitch_list("f c b b")
t8.out("F9")


# Bot 8th
# Pitching: LAA #57 Jerome Williams
b8 = game.new_inning()

# 2. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("P4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("b f c")
b8.out("G4-3")

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.error(7)
b8.reach("E7", end_base=2)

# 5. BOS #12 Mike Napoli (X - 34 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #36 Junichi Tazawa
t9 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
t9.pitching_substitution(36)

# 5. LAA #47 Howie Kendrick (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
t9.advance(2, "10 G1-3")
t9.advance(3, "6 G3")

# 6. LAA #10 Brad Hawpe (X - X - 47)
t9.new_ab()
t9.out("G1-3")

# 7. LAA #6  Alberto Callaspo (X - 47 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b c b")
t9.out("G3")

# 8. LAA #16 Hank Conger (47 - X - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c b s s")
t9.out("K")

# Winning team: BOS
# WP: BOS #11 Clay Buchholz
game.winning_pitcher(11)

# Loser team: LAA
# LP: LAA #33 C.J. Wilson
game.losing_pitcher(33, is_away_team=True)

# print(game)
game.generate_scorecard()
