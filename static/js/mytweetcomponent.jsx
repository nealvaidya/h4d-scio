import React from "react";
import ReactDOM from "react-dom";
import Tweet from 'react-tweet';

class MyTweetComponent extends React.Component {
    render() {
        const tweetData = {
            id_str: 'id_str',
            user: {
                name: this.props.data.name,
                screen_name: this.props.data.username
            },
            text: this.props.data.tweets,
            created_at: this.props.data.ymd,
            favorite_count: 'favorite_count',
            retweet_count: 'retweet_count',
            entities: {
                urls: [],
                user_mentions: [],
                hashtags: [],
                symbols: []
            }
        }

        return (
            <Tweet data={tweetData}/>
        )
    }
}

class TweetContainer extends React.Component {
    constructor(props) {
        super(props);
//        this.state = {data: tweetsData}
    }

    render() {
        const listItems = this.props.data.map(
            (d,i) => 
            <MyTweetComponent key={i} data={d}/>
        );
        return (
            <div>{listItems}</div>
        )

    }
}

export default TweetContainer;