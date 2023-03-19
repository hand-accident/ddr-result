<script>
    let className;
    export { className as class };
</script>

<div class="a {className}">踊</div>
<slot />

<style lang="postcss" module>
    .a {
        @apply inline-flex items-center justify-center transition duration-200 ease-in-out h-6 leading-6 px-2.5
        border rounded-badge border-error border-opacity-50 bg-transparent text-error;
        width: fit-content;
    }
</style>
