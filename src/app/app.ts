import {Component, bootstrap, NgFor} from 'angular2/angular2';

@Component({
    directives: [NgFor]
    selector: 'my-app',
    template: `
    <h1>{{title}}</h1>
    <h2>Products used in this stack are {{myProduct}}</h2>
    <p>Full Stack:</p>
    <ul>
	    <li *ng-for="#product of products">
		    {{product}}
	    </li>
    </ul>
    `
})
export class AppComponent { 
	title = 'epiTWEET';
	products = ['Angular2', 'HTML5', 'CSS3', 'Bootstrap', 'REST', 'Python', 'Flask', 'Git', 'npm'];
	myProduct = this.products[0];
	}

bootstrap(AppComponent);
