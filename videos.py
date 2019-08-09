import csv
import pprint

def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""

    vid_data = []

    #added encoding="utf8" because it was unable to read the csv file
    with open('USvideos.csv', encoding="utf8", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                vid_data.append(vid_dict)
    return vid_data


def print_data(data):
    for entry in data:
        pprint.pprint(entry)


# get the most and least popular channel

def get_most(dictionary):

    return_dict = {'channel_title': None, 'num_total': 0}
    for k,v in dictionary.items():
        if int(v) > return_dict['num_total']:
            return_dict['channel_title'] = k
            return_dict['num_total'] = int(v)
    return return_dict


def get_least(dictionary):

    return_dict = {'channel_title': None, 'num_total': float('Inf')}
    for k,v in dictionary.items():
        if int(v) < return_dict['num_total']:
            return_dict['channel_title'] = k
            return_dict['num_total'] = int(v)
    return return_dict


def get_most_popular_and_least_popular_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    # Output dictionary
    most_popular_and_least_popular_channel = {'most_popular_channel': None,
                                              'least_popular_channel': None,
                                              'most_pop_num_views': None,
                                              'least_pop_num_views': None}
    # Aggregate the number of views of the channels
    aggregate_channel = {}
    for item in data[1:]:
        aggregate_channel.setdefault(item['channel_title'], 0)         # check, create keys and set o as default value
        aggregate_channel[item['channel_title']] += int(item['views']) # update total views of the corresponding channel

    # Get the most and least popular channel in aggregate_channel dictionary, and assign the values
    most_popular_channel_dict = get_most(aggregate_channel)

    most_popular_and_least_popular_channel['most_popular_channel'] = most_popular_channel_dict['channel_title']
    most_popular_and_least_popular_channel['most_pop_num_views'] = most_popular_channel_dict['num_total']

    least_popular_channel_dict = get_least(aggregate_channel)

    most_popular_and_least_popular_channel['least_popular_channel'] = least_popular_channel_dict['channel_title']
    most_popular_and_least_popular_channel['least_pop_num_views'] = least_popular_channel_dict['num_total']

    return most_popular_and_least_popular_channel


def get_most_liked_and_disliked_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    # the output of most like and dislike channel
    most_liked_and_disliked_channel = {'most_liked_channel': None, 'num_likes': None, 'most_disliked_channel': None, 'num_dislikes': None}
    # Aggregate the number of likes and dislikes
    aggregate_channel_likes = {}
    aggregate_channel_dislikes = {}

    # check and set value
    for item in data[1:]:
        aggregate_channel_likes.setdefault(item['channel_title'], 0)
        aggregate_channel_likes[item['channel_title']] += int(item['likes'])
        aggregate_channel_dislikes.setdefault(item['channel_title'], 0)
        aggregate_channel_dislikes[item['channel_title']] += int(item['dislikes'])

    # Get the most liked channel in the dictionary and assign the value
    most_liked_channel_dict = get_most(aggregate_channel_likes)
    most_liked_and_disliked_channel['most_liked_channel'] = most_liked_channel_dict['channel_title']
    most_liked_and_disliked_channel['num_likes'] = most_liked_channel_dict['num_total']

    # Get the most disliked channel in the dictionary and assign the value
    most_disliked_channel_dict = get_most(aggregate_channel_dislikes)
    most_liked_and_disliked_channel['most_disliked_channel'] = most_disliked_channel_dict['channel_title']
    most_liked_and_disliked_channel['num_dislikes'] = most_disliked_channel_dict['num_total']

    return most_liked_and_disliked_channel


if __name__ == '__main__':
    vid_data = get_video_data()

    # uncomment the line below to see what the data looks like
    # print_data(vid_data)

    popularity_metrics = get_most_popular_and_least_popular_channel(vid_data)

    like_dislike_metrics = get_most_liked_and_disliked_channel(vid_data)

    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))