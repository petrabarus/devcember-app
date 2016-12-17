class CommentForm extends React.Component {
    constructor(props) {
        super(props);
    }
    handleSubmit() {
        return false;
    }
    render() {
        return (
            <div className="panel panel-default">
                <div className="panel-body">
                    <form onSubmit={this.handleSubmit}>
                        <div className="form-group">
                            <input type="text" className="form-control" id="name" placeholder="Put your name here"/>
                        </div>
                        <div className="form-group">
                            <textarea className="form-control" rows="3" id="comment" placeholder="Put your comment here"></textarea>
                        </div>
                        <div className="form-group text-right">
                            <input type="submit" value="Submit" className="btn btn-primary"/>
                        </div>
                    </form>
                </div>
            </div>
        );
    }
}

class CommentListItem extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        let comment = this.props.comment;
        let date = new Date(comment.createdAt * 1000);
        let timeLabelOptions = {weekday: "long", year: "numeric", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit"};
        let timeLabel = date.toLocaleDateString("en-US", timeLabelOptions);
        return (
            <div id={comment.id} className="panel panel-default">
                <div className="panel-body">
                    <strong>{comment.name}</strong> on <em>{timeLabel}</em> says <br/>
                    <blockquote>
                        {comment.comment}
                    </blockquote>
                </div>
            </div>
        );
    }
}

class CommentList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {comments: []};
    }
    loadComments() {
        let url = API_BASE_URL + 'comments/list';
        fetch(url)
            .then((response) => {
                return response.json();
            })
            .then((json) => {
                this.setState({comments: json.comments});
            });
    }
    componentDidMount() {
        this.loadComments();
    }
    render() {
        let listItems = this.state.comments.map((comment) =>
            <CommentListItem key={comment.id} comment={comment}/>
        );
        return (
            <div className="panel panel-default">
                <div className="panel-body">
                    {listItems}
                </div>
            </div>
        );
    }
}

ReactDOM.render(<CommentList/>, document.getElementById('comment-list-wrapper'));
ReactDOM.render(<CommentForm/>, document.getElementById('comment-form-wrapper'));
